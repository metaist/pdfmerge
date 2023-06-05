"""Command-line utility for merging, splicing, and rotating PDF documents.

.. include:: ../../README.md
   :start-line: 4
"""

# native
from __future__ import annotations
from dataclasses import dataclass
from dataclasses import field
from getpass import getpass
from glob import glob
from pathlib import Path
from typing import Any
from typing import Generic
from typing import List
from typing import Optional
from typing import Sequence
from typing import TypeVar
from typing import Union
import re
import sys

# lib
from pypdf import PdfReader
from pypdf import PdfWriter

__all__ = ("__version__", "pdfmerge")
__version__ = "1.0.0"

ERR_PATH = "ERROR: path not found: {0}"
"""Error when a path is not found."""

ERR_RULE = "ERROR: invalid rule: {0}"
"""Error when an invalid rule is encountered."""

ERR_RANGE = "ERROR: page {0} out of range [1-{1}]"
"""Error when a page is outside of the available ranges."""

ERR_BOUNDS = "ERROR: missing upper bound on range [{0}..]"
"""Error when the upper range is missing."""

# RE_MATCH_TYPE = type(re.match("", ""))
RE_HAS_RULE = re.compile(r"^(.*)\[(.*)\]$")
"""Regex that matches when an input has a rule."""

RE_RULE = re.compile(r"^(-?\d+)?(\.\.)?(-?\d+)?([>V<])?$")
"""Regex that checks that the rule is valid."""

RULE_RANGE = ".."
"""Range indicator."""

RULE_ROTATE = {None: 0, ">": 90, "V": 180, "<": 270}
"""Rotation rules."""

RULE_DEFAULT = RULE_RANGE
"""Default rule is all pages, unrotated."""


T = TypeVar("T")
"""Generic type."""


@dataclass
class Parsed(Generic[T]):
    """Generic set of parsed results."""

    done: List[T] = field(default_factory=list)
    """Items that were parsed without error."""

    errors: List[str] = field(default_factory=list)
    """Errors encountered during parsing."""

    def __add__(self, other: Parsed[Any]) -> Parsed[Any]:
        """Merge this result with another result."""
        return Parsed(self.done + other.done, self.errors + other.errors)

    def __iadd__(self, other: Parsed[Any]) -> Parsed[Any]:
        """Update this result  with data from another result."""
        self.done += other.done
        self.errors += other.errors
        return self


@dataclass
class ParsedPath:
    """Parsed path and its rules."""

    path: Path
    """Path to process."""

    rules: List[str] = field(default_factory=list)
    """Rules to apply."""


def rangify(
    rule: Union[str, re.Match[str]],
    last: int,
) -> Union[List[int], range]:
    """Convert a rule into a range.

    Args:
        rule (str, Match): pages to extract or a regex matching the rule
        last (int): maximum number of pages

    Returns:
        Union[List[int], range]: list or `range` of pages to extract.

    Examples:
        >>> list(rangify('', 3))
        [1, 2, 3]
        >>> list(rangify('1', 10))
        [1]
        >>> list(rangify('1..3', 10))
        [1, 2, 3]
        >>> list(rangify('3..1', 10))
        [3, 2, 1]
        >>> rangify('1..', 5) == rangify('..', 5)
        True
        >>> list(rangify('-3..-1', 5))
        [3, 4, 5]
        >>> list(rangify(RE_RULE.search('5..7'), 3))
        [3]
    """
    result: Union[List[int], range]
    match: Optional[re.Match[str]]

    if isinstance(rule, str):
        match = RE_RULE.search(rule)
        assert match, ERR_RULE.format(rule)
    elif isinstance(rule, re.Match):
        assert rule is not None, ERR_RULE.format()
        match = rule

    if not match:  # pragma: no cover
        return []

    left, has_range, right, _ = match.groups()
    is_range = has_range == RULE_RANGE

    beg, end = 1, last
    if not left and not right:  # [""] => [..]
        is_range = True

    if left:
        beg = int(left)
        if beg < 1:  # too low
            beg += last + 1
        elif beg > last:  # too high
            beg = last

    if right:
        end = int(right)
        if end < 1:  # too low
            end += last + 1
        elif end > last:  # too high
            end = last
    elif is_range:
        end = last

    # Generate ranges:
    if is_range and end < beg:
        result = range(beg, end - 1, -1)
    elif is_range:
        result = range(beg, end + 1)
    else:
        result = [beg]

    return result


def add_path(
    writer: PdfWriter,
    item: ParsedPath,
    password: Optional[str] = None,
) -> PdfWriter:
    """Add some PDF pages to a PDF writer.

    Args:
        writer (PdfFileWriter): writer to add to.
        item (ParsedPath): the path and rules to add.
        password (str, optional): password for encrypted files. Defaults to `None`.

    Returns:
        PdfFileWriter: the writer object
    """
    reader = PdfReader(item.path.open("rb"))
    if reader.is_encrypted:
        if password is None:
            print(f"Reading encrypted PDF <{item.path}>")
            password = getpass()
        reader.decrypt(password)

    for rule in item.rules:
        match = RE_RULE.search(rule)
        assert match, ERR_RULE.format(rule)

        rotate = match.group(4)
        for num in rangify(match, len(reader.pages)):
            writer.add_page(reader.pages[num - 1].rotate(RULE_ROTATE[rotate]))

    return writer


def parse_paths(
    inputs: Sequence[str],
    _rule: Union[str, List[str]] = RULE_DEFAULT,
) -> Parsed[ParsedPath]:
    """Split inputs into `Path` and rules.

    Args:
        inputs (Sequence[str]): inputs to parse

        _rule (str, optional): default rule to apply. Defaults to `RULE_DEFAULT`.

    Returns:
        Parsed:
            - `.done`: contains a list of successfully parsed items
                - `.path`: `Path` to the file
                - `.rules`: list of rules to apply
            - `.errors`: list of errors encountered
    """
    result: Parsed[ParsedPath] = Parsed()

    if isinstance(_rule, str):
        _rule = [_rule]

    for item in inputs:
        ok = True
        path = None
        rules = _rule

        has_rule = RE_HAS_RULE.search(item)
        if has_rule:
            item = has_rule.group(1)
            rules = re.sub(r"\s", "", has_rule.group(2)).split(",")

        for rule in rules:
            if not RE_RULE.search(rule):
                ok, err = False, ERR_RULE.format(rule)
                if err not in result.errors:
                    result.errors.append(err)
        # rules checked

        path = Path(item)
        if path.is_dir():
            paths = [str(p) for p in path.glob("*.pdf")]
            return result + parse_paths(sorted(paths), rules)
        # folder full of PDFs handled

        if "*" in item:
            return result + parse_paths(sorted(glob(item)), rules)
        # glob handled

        if not path.exists():
            ok, err = False, ERR_PATH.format(path)
            if err not in result.errors:
                result.errors.append(err)
        # path checked

        if ok:
            result.done.append(ParsedPath(path=path, rules=rules))

    return result


def pdfmerge(inputs: List[str], output: str, password: Optional[str] = None) -> None:
    """Merge PDFs into a single PDF.

    Args:
        inputs (List[str]): list of paths to merge with optional rules
        output (str): output file name
        password (str, optional): password for encrypted files. Defaults to `None`.
    """
    parsed = parse_paths(inputs)
    if parsed.errors:
        for err in parsed.errors:
            print(err, file=sys.stderr)
        return

    with Path(output).open("wb") as stream:
        with PdfWriter(stream) as writer:
            for item in parsed.done:
                add_path(writer, item, password)


__pdoc__ = {"pdfmerge.__main__": True}

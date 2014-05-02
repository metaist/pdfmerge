#!/usr/bin/python
# coding: utf-8

"""Command-line PDF utility.

Utility for merging, splicing, and rotating PDF documents.
"""

from glob import glob
import argparse
import os
import re

from PyPDF2 import PdfFileWriter, PdfFileReader

__author__ = 'The Metaist'
__copyright__ = 'Copyright 2014, Metaist'
__email__ = 'metaist@metaist.com'
__license__ = 'MIT'
__maintainer__ = 'The Metaist'
__status__ = 'Prototype'
__version__ = '0.0.6'
__version_info__ = tuple(__version__.split('.'))

ERROR_PATH = 'ERROR: path not found: {0}'
ERROR_RULE = 'ERROR: invalid rule: {0}'
ERROR_RANGE = 'ERROR: page {0} out of range [1-{1}]'
ERROR_BOUNDS = 'ERROR: missing upper bound on range [{0}..]'

RE_MATCH_TYPE = type(re.match('', ''))
RE_HAS_RULE = re.compile(r'^(.*)\[(.*)\]$')
RE_RULE = re.compile(r'^(-?\d+)?(\.\.)?(-?\d+)?([>V<])?$')

RULE_RANGE = '..'
RULE_ROTATE = {None: 0, '>': 90, 'V': 180, '<': 270}  # rotation rules
RULE_DEFAULT = RULE_RANGE  # all pages, unrotated


def rangify(rule, range_max=None):
    """Convert a rule into a range.

    Args:
        rule (str, obj): pages to extract or a regex matching the rule
        range_max (int): maximum number of pages

    Returns:
        (list). List of pages to extract.

    Examples:
        >>> rangify('', 3)
        [1, 2, 3]
        >>> rangify('1')
        [1]
        >>> rangify('1..3')
        [1, 2, 3]
        >>> rangify('3..1')
        [3, 2, 1]
        >>> rangify('1..', 5) == rangify('..', 5) == rangify('..5')
        True
        >>> rangify('-3..-1', 5)
        [3, 4, 5]
        >>> rangify(RE_RULE.search('5..7'), 3)
        [3]
    """
    # pylint: disable=R0912
    result, match = [], None
    if type(rule) is str:
        match = RE_RULE.search(rule)
        assert match, ERROR_RULE.format(rule)
    elif type(rule) is RE_MATCH_TYPE:
        assert rule is not None, ERROR_RULE.format()
        match = rule

    beg, isrange, end, _ = match.groups()
    isrange = (isrange == RULE_RANGE)

    if not beg and not end:
        assert range_max is not None, ERROR_BOUNDS.format(beg)
        beg, isrange, end = 1, True, range_max

    beg = (beg and int(beg)) or 1
    end = (end and int(end))

    if beg:
        beg = int(beg)
        if range_max and beg < 1:
            beg += range_max + 1
        elif range_max and beg > range_max:
            beg = range_max

    if end:
        end = int(end)
        if range_max and end < 1:
            end += range_max + 1
        elif range_max and end > range_max:
            end = range_max
    elif isrange:
        assert range_max is not None, ERROR_BOUNDS.format(beg)
        end = range_max

    # Generate ranges:
    if isrange and end < beg:
        result = sorted(range(end, beg + 1), reverse=True)
    elif isrange:
        result = range(beg, end + 1)
    else:
        result.append(beg)

    return result


def add(path, writer=None, rules=RULE_DEFAULT):
    """Add one or more paths to a PdfFileWriter.

    Args:
        path (str, list):       path or list of paths to merge
        writer (PdfFileWriter): output writer to add pdf files
        rules (str):            pages and rotation rules

    Returns:
        (PdfFileWriter). The merged PDF ready for output.
    """
    if writer is None:
        writer = PdfFileWriter()

    if type(path) is list:  # merge all the paths
        for subpath in path:
            writer = add(subpath, writer, rules)
    else:
        match = RE_HAS_RULE.search(path)
        if match:
            path, rules = match.groups()
        rules = re.sub(r'\s', '', rules)  # remove all whitespace

        if os.path.isdir(path):  # merge all pdfs in a directory
            path = os.path.join(path, '*.pdf')

        if '*' in path:  # merge multiple files
            writer = add(glob(path), writer, rules)
        else:  # base case; a single file
            assert os.path.isfile(path), ERROR_PATH.format(path)
            reader = PdfFileReader(file(path, 'rb'))
            for rule in rules.split(','):
                match = RE_RULE.search(rule)
                assert match, ERROR_RULE.format(rule)
                _, _, _, rotate = match.groups()
                for page in rangify(match, reader.getNumPages()):
                    writer.addPage(
                        reader.getPage(page - 1).rotateClockwise(
                            RULE_ROTATE[rotate]
                        )
                    )
    return writer


def merge(paths, output):  # pragma: no cover
    """Merge the paths into a single PDF.

    Args:
        paths (list): list of paths to merge
        output (str): output file name
    """
    writer = add(paths)
    with file(output, 'wb') as stream:
        writer.write(stream)


def main(args=None):    # pragma: no cover
    """Main entry point."""
    parser = argparse.ArgumentParser(description=__doc__, prog='pdfmerge',
                                     fromfile_prefix_chars='@')
    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('paths', metavar='PATH', nargs='+',
                        help='PDF files to merge')
    parser.add_argument('-o', '--output', metavar='FILE', default='output.pdf',
                        help='output file (default: "%(default)s")')
    opts = parser.parse_args(args)  # command-line args parsed
    merge(opts.paths, opts.output)  # paths merged


if __name__ == '__main__':  # pragma: no cover
    main()

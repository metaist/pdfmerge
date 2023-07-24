# pdfmerge

_Command-line utility for merging, splicing, and rotating PDF documents._

[![Build Status](https://img.shields.io/github/actions/workflow/status/metaist/pdfmerge/.github/workflows/ci.yaml?branch=main&style=for-the-badge)](https://github.com/metaist/pdfmerge/actions)
[![pdfmerge on PyPI](https://img.shields.io/pypi/v/pdfmerge.svg?color=blue&style=for-the-badge)](https://pypi.org/project/pdfmerge)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pdfmerge?style=for-the-badge)](https://pypi.org/project/pdfmerge)

[Changelog] - [Issues] - [Documentation]

[changelog]: https://github.com/metaist/pdfmerge/blob/main/CHANGELOG.md
[issues]: https://github.com/metaist/pdfmerge/issues
[documentation]: https://metaist.github.io/pdfmerge/

## Why?

I find myself merging bits of different PDFs fairly regularly and really wanted a simple CLI way to do it.

## Install

```bash
python -m pip install pdfmerge
```

## Usage

    $ pdfmerge [-h] [--version] [-o FILE|--output FILE] [-p PASSWORD|--password PASSWORD] PATH[RULE[, RULE ...]] [PATH[RULE, ...]] ...]

- `-o`, `--output` output file (default: `output.pdf`).
- `-p`, '--password` password for encrypted files (default: empty string).
- `PATH` a file, directory, or wildcard string (e.g., `file*.pdf`) of files
  to merge.
- `RULE` an optional string indicating which pages to extract and rotate.
  The syntax for each rule is:

      [START][..][END][ROTATE]

  Where `START` and `END` are positive (1-based) or negative page numbers and
  `ROTATE` is one of `>`, `V`, or `<` indicating a clockwise rotation of
  90, 180, 270 degrees, respectively.

## Command-line Example

    $ pdfmerge -o out.pdf file1.pdf file2.pdf[3,3] file2.pdf[1V,2..-1] "other*.pdf[<]" "/path/pdf[1..4>,5]"

This example illustrates several features:

- specifying an output file (must not be any of the input files)
- merging multiple files, some more than once
- splicing parts of file using indices (1-based; negatives allowed)
- including the same page multiple times
- rotating a page or page range
- merging all the PDFs in a directory

[Read more about the options](https://metaist.github.io/pdfmerge/__main__.html)

# Python Module Usage

`pdfmerge` can also be imported into python scripts.

```python
from pdfmerge import pdfmerge
pdfmerge(["pdf-1.pdf", "pdf-2.pdf[2>]"], "output.pdf")
```

## License

[MIT License](https://github.com/metaist/pypdf/blob/main/LICENSE.md)

[ci-image]: https://travis-ci.org/metaist/pdfmerge.png?branch=master
[ci-status]: http://travis-ci.org/metaist/pdfmerge
[gh-code]: https://github.com/metaist/pdfmerge/zipball/master
[gh-issues]: https://github.com/metaist/pdfmerge/issues
[gh-issues-all]: https://github.com/metaist/pdfmerge/issues/search?q=
[gh-pdfmerge]: https://github.com/metaist/pdfmerge/blob/master/pdfmerge.py
[gh-setup]: https://github.com/metaist/pdfmerge/blob/master/releases/pdfmerge-latest-setup.exe
[osi-mit]: http://opensource.org/licenses/MIT
[pypdf]: https://pypi.python.org/pypi/pyPdf

# pdfmerge: CLI for merging, splicing, and rotating PDFs

<p align="center">
  <a href="https://metaist.github.io/pdfmerge/"><img alt="pdfmerge" width="200" src="https://raw.githubusercontent.com/metaist/pdfmerge/main/staple-the-squirrel.png" /></a><br />
  <em>Staple the Squirrel</em>
</p>
<p align="center">
  <a href="https://github.com/metaist/pdfmerge/actions/workflows/ci.yaml"><img alt="Build" src="https://img.shields.io/github/actions/workflow/status/metaist/pdfmerge/.github/workflows/ci.yaml?branch=main&logo=github"/></a>
  <a href="https://pypi.org/project/pdfmerge"><img alt="PyPI" src="https://img.shields.io/pypi/v/pdfmerge.svg?color=blue" /></a>
  <a href="https://pypi.org/project/pdfmerge"><img alt="Supported Python Versions" src="https://img.shields.io/pypi/pyversions/pdfmerge" /></a>
</p>

## Why?

I find myself merging bits of different PDFs fairly regularly and really wanted a simple CLI way to do it.

## Install

```bash
python -m pip install pdfmerge
```

## Usage

    $ pdfmerge [-h] [--version]
      [-o FILE|--output FILE]
      [-p PASSWORD|--password PASSWORD]
      PATH[RULE[, RULE ...]] [[PATH[RULE, ...]] ...]

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

- specifying an output file
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

[MIT License](https://github.com/metaist/pdfmerge/blob/main/LICENSE.md)

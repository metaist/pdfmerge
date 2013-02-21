# pdfmerge [![Build Status][ci-image]][ci-status]
`pdfmerge` is a command-line utility for manipulating PDF files.

## Getting Started
Clone the repository via `git clone git://github.com/metaist/pdfmerge.git`
or get [the latest code](https://github.com/metaist/pdfmerge/zipball/master).

Get the dependencies (primarly [pyPdf][pypdf]) using `ant` or `pip`:

    $ ant resolve
    $ pip install -r requirements.txt --use-mirrors
    
You can test the package using `ant`:

    $ ant test

## Command-line Examples
Merge multiple files together:

    $ pdfmerge.py file1.pdf file2.pdf
    $ pdfmerge.py file*.pdf

Extract or reorder one or more pages from one or more files:

    $ pdfmerge.py file.pdf[2]
    $ pdfmerge.py file.pdf[2, 1, 3]
    $ pdfmerge.py file.pdf[1..3, 7..10]
    $ pdfmerge.py file.pdf[3..1]
    $ pdfmerge.py file.pdf[1, 4..]
    $ pdfmerge.py file*.pdf[7]

Rotate indivial pages or ranges (use `>`, `V`, and `<` to rotate 90, 180, and 270
degrees clockwise). Remember to use quotes around the path to avoid command-line
issues:

    $ pdfmerge.py "file.pdf[1..3>]" (range rotated 90 degrees clockwise)
    $ pdfmerge.py "file.pdf[1<]" (rotated 90 degrees counter-clockwise)
    $ pdfmerge.py "file.pdf[1..2, 4V]" (rotated 180 degrees clockwise)
    $ pdfmerge.py "*.pdf[>]" (all pages in all pdfs rotate 90 degrees clockwise)

## Code Examples
`pdfmerge` can also be included in python scripts.

    import pdfmerge
    pdfmerge.merge(['pdf-1.pdf', 'pdf-2.pdf[2>]'], 'output.pdf')

## License
Licensed under the [MIT License][osi-mit].

[ci-image]: https://secure.travis-ci.org/metaist/pdfmerge.png
[ci-status]: http://travis-ci.org/metaist/pdfmerge
[osi-mit]: http://opensource.org/licenses/MIT
[pypdf]: https://pypi.python.org/pypi/pyPdf

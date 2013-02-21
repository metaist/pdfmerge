# pdfmerge [![Build Status][ci-image]][ci-status]
pdfmerge is a command-line utility for manipulating PDF files.

## Getting Started
Clone the repository via `git clone git://github.com/metaist/pdfmerge.git`
or get [the latest code](https://github.com/metaist/pdfmerge/zipball/master).

## Examples
Merge multiple files together:

    pdfmerge file1.pdf file2.pdf
    pdfmerge file*.pdf

Extract or reorder one or more pages from one or more files:

    pdfmerge file.pdf[2]
    pdfmerge file.pdf[2, 1, 3]
    pdfmerge file.pdf[1..3, 7..10]
    pdfmerge file.pdf[3..1]
    pdfmerge file.pdf[1, 4..]
    pdfmerge file*.pdf[7]

Rotate indivial pages or ranges (use >, V, < to rotate 90, 180, and 270 degrees
clockwise):

    pdfmerge file.pdf[1..3>] (range rotated 90 degrees clockwise)
    pdfmerge file.pdf[1<] (rotated 90 degrees counter-clockwise)
    pdfmerge file.pdf[1..2, 4V] (rotated 180 degrees clockwise)
    pdfmerge *.pdf[>]

## License
Licensed under the [MIT License][osi-mit].

[ci-image]: https://secure.travis-ci.org/metaist/pdfmerge.png
[ci-status]: http://travis-ci.org/metaist/pdfmerge
[osi-mit]: http://opensource.org/licenses/MIT
[semver]: http://semver.org/

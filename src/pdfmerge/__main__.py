#!/usr/bin/python
# coding: utf-8
"""pdfmerge - Merge, splice, and rotate PDFs.

```
Usage: pdfmerge [--help|--version] <path>... [-p PASSWORD][-o FILE]

Options:
  -h, --help                  display this message and exit
  --version                   display the version and exit

  <path>                      paths to PDFs to merge
  -p PASS, --password PASS    password to decrypt PDFs
  -o FILE, --output FILE      output file [default: output.pdf]
                              NOTE: this may not be any of the input files
```

After each `<path>`, there are some optional rules you apply. These are written
in brackets after the file name. Remember to put quotes around the file name so
that your shell doesn't interpret the brackets incorrectly.

## Use index-like notation to choose page ranges

After each `<path>`, specify which parts of the file should be spliced.

```bash
  $ pdfmerge file1.pdf[1] file2.pdf[2]
  $ pdfmerge file*.pdf[7]
  $ pdfmerge file.pdf[3..1]
  $ pdfmerge "file.pdf[1..3, 7..10]"
  $ pdfmerge "file.pdf[2, 1, 3]"
  $ pdfmerge "file.pdf[1, 4..]"
```

- If indices are omitted, all pages are included.
- Use commas to separate multiple ranges.
- Whitespace is ignored (e.g., `[1 .. 2, 3]` is the same as `[1..2,3]`), but
  remember to enclose parameters with whitespace.
- **Indices start at 1** (1-based), but negative indices are ok
    (i.e. the first page is `1`, not `0`; `-1` is the last page).
- Reverse ranges are ok (e.g., `[2..1]` is the reverse of `[1..2]`).
- Open-ended ranges are ok (e.g., `[2..]` and `[..3]`).
- Ranges outside of bounds are _quietly_ forced into bounds
    (e.g., `[2..7]` for a 3-page file is treated like `[2..3]`).

## Rotate individual pages or page ranges

After each range, use a rotator (`>`, `V`, and `<`) to rotate the range by
90, 180, and 270 degrees clockwise.

```bash
  $ pdfmerge "file.pdf[1..3>]"
  $ pdfmerge "file.pdf[1<]"
  $ pdfmerge file.pdf[1..2, 4V]
  $ pdfmerge "*.pdf[>]"
```

- When using the `<` and `>` rotators, surround the entire string
  with quotes to avoid conflicts with the command-line's use of those operators.
- The rotator is case-sensitive (i.e. it's a capital `V`).
- You cannot specify more than one rotator. (Why would you want that?)
- The rotator comes right after the range (e.g., `[1>,2..3]` not `[1>..3]`).
- You can still specify a rotator if there's no range (e.g., `[<]` is the
  same as `[1..<]`).
"""
# native
from typing import cast
from typing import List
from typing import Optional
from typing import Sequence

# lib
from attrbox import parse_docopt

# pkg
from . import __version__
from . import pdfmerge


def main(argv: Optional[Sequence[str]] = None) -> None:  # pragma: no cover
    """Main entry point."""
    args = parse_docopt(__doc__, argv, version=__version__)
    pdfmerge(
        cast(List[str], args.path),
        cast(str, args.output),
        args.password,
    )


if __name__ == "__main__":
    main()

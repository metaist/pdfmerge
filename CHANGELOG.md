# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog] and this project adheres to [Semantic Versioning].

Sections order is: `Fixed`, `Changed`, `Added`, `Deprecated`, `Removed`, `Security`.

[keep a changelog]: http://keepachangelog.com/en/1.0.0/
[semantic versioning]: http://semver.org/spec/v2.0.0.html

---

## [Unreleased]

[unreleased]: https://github.com/metaist/pdfmerge/compare/prod...main

These are changes that are on `main` that are not yet in `prod`.

---

[#13]: https://github.com/metaist/pdfmerge/issues/13
[#15]: https://github.com/metaist/pdfmerge/pull/15
[#19]: https://github.com/metaist/pdfmerge/pull/19
[#20]: https://github.com/metaist/pdfmerge/pull/20
[#21]: https://github.com/metaist/pdfmerge/issues/21
[#23]: https://github.com/metaist/pdfmerge/issues/23
[#24]: https://github.com/metaist/pdfmerge/issues/24
[#25]: https://github.com/metaist/pdfmerge/issues/25
[1.0.0]: https://github.com/metaist/pdfmerge/compare/0.0.7...1.0.0

## [1.0.0] - 2023-06-05T12:03:55Z

**Fixed**

- [#15]: use `isinstance()` instead of `type()` (by @begert)
- [#20]: `print` on python 3 (by @lukasbindreiter)

**Changed**

- [#19]: upgraded to python 3 (by @arjndr)
- [#23]: supported python version (3.8, 3.9, 3.10, 3.11)
- [#24]: directory structure (`src` layout, using `pyproject.toml`) and other cleanup

**Added**

- [#13]: prompt for password for encrypted PDFs (if not supplied on CLI)
- [#21]: complete docs in `--help`

**Removed**

- [#25]: Windows-specific builds
- `pdfmerge.add`, `pdfmerge.merge`

---

[#12]: https://github.com/metaist/pdfmerge/pull/12
[0.0.7]: https://github.com/metaist/pdfmerge/compare/0.0.6...0.0.7

## [0.0.7] - 2015-01-01T03:28:13Z

**Fixed**

- [#12]: installing `pdfmerge` when `PyPDF2` is not installed

**Added**

- [#12]: decrypting PDFs

---

[0.0.6]: https://github.com/metaist/pdfmerge/compare/0.0.5...0.0.6

## [0.0.6] - 2014-05-02T02:11:13Z

**Removed**

- unnecessary dependencies to make sure `pip install pdfmerge` works correctly

---

[#11]: https://github.com/metaist/pdfmerge/issues/11
[0.0.5]: https://github.com/metaist/pdfmerge/commits/0.0.5

## [0.0.5] - 2014-05-02T01:19:20Z

**Changed**

- [#11]: Upgraded to `PyPDF2`

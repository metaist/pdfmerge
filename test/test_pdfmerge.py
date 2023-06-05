"""Test pdfmerge."""

# native
from pathlib import Path

# pkg
# import pdfmerge

TEST_PDF_DIR = Path("test") / "pdfs"
TEST_PDF_1 = TEST_PDF_DIR / "test-1.pdf"
TEST_PDF_2 = TEST_PDF_DIR / "test-2.pdf"


# def test_pass_single() -> None:
#     """A non-merge."""
#     writer = pdfmerge.add(TEST_PDF_1)
#     self.assertTrue(writer is not None)
#     self.assertTrue(1, writer.getNumPages())

# def test_merge_dir(self):
#     """Merge all PDFs in a directory."""
#     writer = pdfmerge.add(TEST_PDF_DIR, password="test")
#     self.assertTrue(writer is not None)
#     self.assertTrue(4, writer.getNumPages())

# def test_rule(self):
#     """Merge part of a PDF."""
#     writer = pdfmerge.add(TEST_PDF_2 + "[2]")
#     self.assertTrue(writer is not None)
#     self.assertTrue(1, writer.getNumPages())

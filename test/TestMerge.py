#!/usr/bin/python
# coding: utf-8

import os
import unittest

import pdfmerge

TEST_PDF_DIR = os.path.join('test', 'pdfs')
TEST_PDF_1 = os.path.join(TEST_PDF_DIR, 'test-1.pdf')
TEST_PDF_2 = os.path.join(TEST_PDF_DIR, 'test-2.pdf')


class TestMerge(unittest.TestCase):
    def test_pass_single(self):
        """A non-merge."""
        writer = pdfmerge.add(TEST_PDF_1)
        self.assertTrue(writer is not None)
        self.assertTrue(1, writer.getNumPages())

    def test_merge_dir(self):
        """Merge all PDFs in a directory."""
        writer = pdfmerge.add(TEST_PDF_DIR)
        self.assertTrue(writer is not None)
        self.assertTrue(3, writer.getNumPages())

    def test_rule(self):
        """Merge part of a PDF."""
        writer = pdfmerge.add(TEST_PDF_2 + '[2]')
        self.assertTrue(writer is not None)
        self.assertTrue(1, writer.getNumPages())

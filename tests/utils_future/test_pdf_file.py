import os
import unittest

from utils_future import PDFFile

TEST_PDF_FILE = PDFFile(os.path.join("tests", "input", "si.pdf"))


class TestCase(unittest.TestCase):

    def test_extract_text(self):
        text = TEST_PDF_FILE.extract_text()
        self.assertEqual(len(text), 4_425)

        lines = text.splitlines()
        non_empty_lines = [line for line in lines if line.strip()]
        self.assertIn(
            non_empty_lines[0],
            "ප ොලිස් මොධ්‍ය  ප ොට්ඨොසය පෙත ෙොතතො වූ ෙැදගත් පතොරතුරු  ",
        )

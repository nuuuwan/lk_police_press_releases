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
        self.assertEqual(
            non_empty_lines[0],
            "ප ොලිස් මොධ්‍ය  ප ොට්ඨොසය පෙත ෙොතතො වූ ෙැදගත් පතොරතුරු  ",
        )

    def test_extract_metadata(self):
        metadata = TEST_PDF_FILE.extract_metadata()

        self.assertEqual(metadata.author, "Police Media Division - E News")
        self.assertEqual(metadata.creator, "Microsoft® Word LTSC")
        self.assertEqual(metadata.producer, "iLovePDF")

        self.assertEqual(
            str(metadata.creation_date), "2025-09-03 10:27:25+05:30"
        )
        self.assertEqual(
            str(metadata.modification_date), "2025-09-03 12:08:27+00:00"
        )

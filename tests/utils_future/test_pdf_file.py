import os
import unittest

from utils_future import PDFFile

TEST_PDF_FILE = PDFFile(os.path.join("tests", "input", "si.pdf"))


class TestCase(unittest.TestCase):

    def test_get_block_info_list(self):
        block_info_list = TEST_PDF_FILE.get_block_info_list()
        self.assertTrue(len(block_info_list), 10)
        first_block = block_info_list[0]

        self.assertEqual(
            first_block,
            {
                "page_number": 0,
                "bbox": (72.02, 136.23, 526.93, 457.57),
                "text": "ප ොලිස් මොධ්\u200dය ප ොට්ඨොසය පෙත ෙොතතො වූ ෙැදගත් පතොරතුරු 01. පෙඩි තබො මනුෂ්\u200dය ඝොතනය ට තැත් කිරීමට සම්බන්ධ්\u200d සැ රුපෙකු අත්අඩංගුෙට - ප ොලිස් විප ්ෂ්\u200d ොයත බල ො තලෙ ැපේ ඳවුර. 2025.09.01 ෙන දින මීටියොපගොඩ ප ොලිස් ෙසපම් මලෙැන්න ොර ප්\u200dරපේ පේදී පුේගලපයකුට පෙඩි තබො ඝොතනය කිරීමට තැත් කිරීපම් අ රොධ්\u200dය සම්බන්ධ්\u200dපයන් මීටියොපගොඩ ප ොලිස් ස්ථොනය මගින් විම තන ආරම්භ ර තිබිණි. 2025.09.02 ෙන දින සෙස් ොලපේ තලෙ ැපේ ප ොලිස් ෙසපම්දී ප ොලිස් විප ්ෂ්\u200d ොයත බල ො තලෙ ැපේ ඳවුපත නිලධ්\u200dොරින් ණ්ඩොයමක් විසින් ලද පතොරතුරක් මත ඉහත අ රොධ්\u200dයට ආධ්\u200dොර අනුබල දුන් සැ රුපෙකු අත්අඩංගුෙට පගන ආගර තන ප ොලිස් ස්ථොනය පෙත ඉදිරි ත් ර ඇත. අත්අඩංගුෙට ගත් සැ රු ෙයස අවුරුදු 31 ක් ෙන ළිඳුල ප්\u200dරපේ පේ දිංචි රුපෙකි.",  # noqa: E501
                "fonts": ["IskoolaPota"],
                "sizes": [
                    6.960000038146973,
                    8.039999961853027,
                    9.960000038146973,
                    14.039999961853027,
                ],
            },
        )

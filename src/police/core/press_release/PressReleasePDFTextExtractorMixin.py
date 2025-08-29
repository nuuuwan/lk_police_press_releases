import os
from functools import cached_property

from utils import File, Log

from utils_future import PDFFile

log = Log("PressReleasePDFTextExtractorMixin")


class PressReleasePDFTextExtractorMixin:
    @cached_property
    def block_text_path(self):
        return os.path.join(self.dir_press_release, "text.block.txt")

    @property
    def has_block_text(self):
        return os.path.exists(self.block_text_path)

    def extract_text(self):
        if self.has_block_text:
            return self.block_text_path
        if not self.has_pdf:
            return None

        block_text = PDFFile(self.pdf_path).extract_text()
        File(self.block_text_path).write(block_text)
        log.info(f"Wrote {self.block_text_path}")

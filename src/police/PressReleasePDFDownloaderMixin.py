import os
from functools import cached_property

from utils import Log

from utils_future import PDFFile

log = Log("PressReleasePDFDownloaderMixin")


class PressReleasePDFDownloaderMixin:
    @cached_property
    def pdf_path(self):
        return os.path.join(self.dir_press_release, "si.pdf")

    @property
    def has_pdf(self):
        return os.path.exists(self.pdf_path)

    def download_pdf(self):
        if self.has_pdf:
            return self.pdf_path
        pdf_file = PDFFile.download(self.url_pdf, self.pdf_path)
        return pdf_file

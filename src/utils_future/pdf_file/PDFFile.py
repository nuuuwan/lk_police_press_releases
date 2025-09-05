import requests
from utils import File, Log

from utils_future.pdf_file.PDFTextMixin import PDFTextMixin

log = Log("PDFFile")


class PDFFile(File, PDFTextMixin):

    def __init__(self, path):
        assert path.endswith(".pdf")
        super().__init__(path)

    @classmethod
    def download(cls, url: str, pdf_path: str):
        response = requests.get(url, timeout=120, verify=False)
        response.raise_for_status()
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        log.info(f"Downloaded PDF to {pdf_path}")
        return cls(pdf_path)

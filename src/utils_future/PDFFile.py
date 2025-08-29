import requests
import urllib3
from utils import Log

from utils_future.FileOrDirFuture import FileOrDirFuture

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


log = Log("PDFFile")


class PDFFile(FileOrDirFuture):

    @staticmethod
    def download(url: str, pdf_path: str) -> "PDFFile":
        response = requests.get(url, timeout=120, verify=False)
        if not response.status_code == 200:
            raise ValueError(f"Failed to download PDF from {url}")

        with open(pdf_path, "wb") as f:
            f.write(response.content)
        pdf_file = PDFFile(pdf_path)
        log.info(f"Wrote {pdf_file}")
        return pdf_file

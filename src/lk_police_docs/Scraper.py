import os
import time

from utils import Log

from utils_future import WebPage

log = Log('Scraper')


class Scraper:
    BASE_URL = 'https://www.police.lk/?p=9472'
    DIR_DATA_PDF = os.path.join('data', 'pdfs')

    def __init__(self, max_delta_t: int):
        self.max_delta_t = max_delta_t

    def run(self):
        time_start = time.time()
        page = WebPage(self.BASE_URL)
        for pdf_page in page.gen_pdfs_recursive():
            pdf_path = os.path.join(self.DIR_DATA_PDF, f'{pdf_page.hash}.pdf')

            if not os.path.exists(self.DIR_DATA_PDF):
                os.makedirs(self.DIR_DATA_PDF, exist_ok=True)

            if os.path.exists(pdf_path):
                continue

            pdf_page.download_binary(pdf_path)
            delta_t = time.time() - time_start
            if delta_t > self.max_delta_t:
                log.info(
                    f"🛑 Stopping. ⏰ {delta_t:.0f}s > {self.max_delta_t:.0f}s."
                )
                break

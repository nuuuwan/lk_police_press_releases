from queue import Queue
from typing import Generator

from utils import Log

from police.PolicePressReleasePage import PolicePressReleasePage
from utils_future import WWW

log = Log("PolicePressReleaseHomePage")


class PolicePressReleaseHomePage(WWW):
    def __init__(self):
        super().__init__("https://www.police.lk/?page_id=657")

    def __get_latest_pr_page_url__(self):
        a = self.soup.find("a", attrs={"press-release": True})
        if not a:
            raise ValueError("No press release link found")
        return a["href"]

    def get_latest_pr_page(self):
        return PolicePressReleasePage(self.__get_latest_pr_page_url__())

    def gen_dicts(self) -> Generator[dict, None, None]:
        page = self.get_latest_pr_page()
        page_queue = Queue()
        page_queue.put(page)
        visited_pages = set()
        while not page_queue.empty():
            page = page_queue.get()
            if page in visited_pages:
                continue
            visited_pages.add(page)
            yield from page.get_gen_dicts()

            for page in [
                page.get_more_page(),
                page.get_prev_page(),
            ]:
                if page and page not in visited_pages:
                    page_queue.put(page)

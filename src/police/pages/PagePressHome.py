from queue import Queue

from utils import Log

from police.pages.PagePR import PagePR
from utils_future import WebPage

log = Log("PagePressHome")


class PagePressHome(WebPage):
    def __init__(self):
        super().__init__("https://www.police.lk/?page_id=657")

    def __get_latest_pr_page_url__(self):
        a = self.soup.find("a", attrs={"press-release": True})
        if not a:
            raise ValueError("No press release link found")
        return a["href"]

    def get_latest_pr_page(self):
        return PagePR(self.__get_latest_pr_page_url__())

    def spider(self, limit):
        log.info(f"Starting 🕷️ spider with {limit=}")
        page = self.get_latest_pr_page()
        page_queue = Queue()
        page_queue.put(page)
        visited_pages = set()
        pr_list = []
        while page_queue.not_empty and len(pr_list) < limit:
            page = page_queue.get()
            visited_pages.add(page)

            log.debug(f"Scraping {page}")
            pr_list_for_page = page.get_pr_list()
            pr_list.extend(pr_list_for_page)

            for page in [page.get_more_page(), page.get_prev_page()]:
                if page and page not in visited_pages:
                    page_queue.put(page)

        log.info(f"🕷️ Spidered {len(pr_list)} press releases")
        return pr_list

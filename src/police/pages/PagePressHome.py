import time
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

    def spider(self, max_dt):
        log.info(f"Starting 🕷️ spider with {max_dt=}s")
        page = self.get_latest_pr_page()
        page_queue = Queue()
        page_queue.put(page)
        visited_pages = set()
        press_release_list = []
        t_start = time.time()
        while True:
            dt = time.time() - t_start

            if page_queue.empty():
                log.info("🛑 No more pages to visit, Stopping 🕷️ spider")
                break

            if dt > max_dt:
                log.info(
                    f"🛑 Reached {dt:.1f} s> {max_dt}s. Stopping 🕷️ spider"
                )
                break

            page = page_queue.get()
            visited_pages.add(page)

            n_press_releases = len(press_release_list)
            log.debug(f"Scraping {page} ({n_press_releases=:,})")
            try:
                press_release_list_for_page = page.get_press_release_list()
                press_release_list.extend(press_release_list_for_page)

                for page in [page.get_more_page(), page.get_prev_page()]:
                    if page and page not in visited_pages:
                        page_queue.put(page)
            except Exception as e:
                log.error(f"Error scraping {page}: {e}")

        log.info(f"🕷️ Spidered {len(press_release_list)} press releases")
        return press_release_list

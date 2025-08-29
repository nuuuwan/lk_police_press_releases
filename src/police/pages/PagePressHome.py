from police.pages.PagePR import PagePR
from utils_future import WebPage


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

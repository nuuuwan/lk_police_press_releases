from utils import Log

from police.core.PressRelease import PressRelease
from utils_future import Parse, WebPage

log = Log("PagePR")


class PagePR(WebPage):

    def __gen_div_date_list__(self):
        div_list = self.soup.find_all(
            "div",
            attrs={"data-element_type": "container"},
        )
        for div in div_list:
            h3_list = div.find_all("h3", class_="elementor-icon-box-title")
            if len(h3_list) != 1:
                continue
            yield div, h3_list[0]

    @staticmethod
    def __parse_div_date_list__(div, h3):
        date_str = h3.get_text(strip=True)
        h5_list = div.find_all("h5")
        for h5 in h5_list:
            time_str = h5.get_text(strip=True)
            time = Parse.time(
                f"{date_str} {time_str}".replace("hrs.", "")[:15]
            )

            a = h5.find("a")
            if not a:
                continue
            url_pdf = a["href"]
            assert url_pdf.lower().endswith(".pdf")
            pr = PressRelease(time=time, url_pdf=url_pdf)
            pr.write()
            yield pr

    @staticmethod
    def __dedupe_and_sort_press_release_list__(press_release_list):
        idx = {pr.time: pr for pr in press_release_list}
        press_release_list = list(idx.values())
        press_release_list.sort(key=lambda pr: pr.time)
        return press_release_list

    def get_press_release_list(self) -> list[PressRelease]:
        press_release_list = []
        for div, h3 in self.__gen_div_date_list__():
            press_release_list.extend(self.__parse_div_date_list__(div, h3))

        press_release_list = self.__dedupe_and_sort_press_release_list__(
            press_release_list
        )
        log.debug(
            f"[{self}] Extracted {len(press_release_list)} press releases"
        )
        return press_release_list

    def __get_labelled_page__(self, label):
        a_list = self.soup.find_all("a")
        for a in a_list:
            span = a.find("span", text=label)
            if span:
                return PagePR(a["href"])
        log.debug(f"[{self}] '{label}' link not found")
        return None

    def get_more_page(self) -> "PagePR":
        return self.__get_labelled_page__("More")

    def get_prev_page(self) -> "PagePR":
        return self.__get_labelled_page__("Previous")

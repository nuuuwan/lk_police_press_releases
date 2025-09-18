from typing import Generator

from utils import Log

from utils_future import WWW, Parse

log = Log("PolicePressReleasePage")


class PolicePressReleasePage(WWW):

    def __gen_div_date_list__(self):
        if not self.soup:
            return
        div_list = self.soup.find_all(
            "div",
            attrs={"data-element_type": "container"},
        )
        for div in div_list:
            h3_list = div.find_all("h3", class_="elementor-icon-box-title")
            if len(h3_list) != 1:
                continue
            yield div, h3_list[0]

    def __get_labelled_page__(self, label):
        soup = self.soup
        if not soup:
            return None
        a_list = soup.find_all("a")
        for a in a_list:
            span = a.find("span", text=label)
            if span:
                return PolicePressReleasePage(a["href"])
        return None

    def get_more_page(self) -> "PolicePressReleasePage":
        return self.__get_labelled_page__("More")

    def get_prev_page(self) -> "PolicePressReleasePage":
        return self.__get_labelled_page__("Previous")

    def get_next_page(self) -> "PolicePressReleasePage":
        return self.__get_labelled_page__("Next")

    def __gen_dicts_from_div_date_list__(
        self, div, h3
    ) -> Generator[dict, None, None]:
        date_str = h3.get_text(strip=True)
        h5_list = div.find_all("h5")
        for h5 in h5_list:
            time_str_raw = h5.get_text(strip=True)
            time_str = Parse.time_str(
                f"{date_str} {time_str_raw}".replace("hrs.", "")[:15]
            )

            a = h5.find("a")
            if not a:
                continue
            url_pdf = a["href"]
            assert url_pdf.lower().endswith(".pdf")
            yield dict(
                time_str=time_str, url_metadata=self.url, url_pdf=url_pdf
            )

    def gen_dicts(self) -> Generator[dict, None, None]:
        log.debug("Processing PolicePressReleasePage: " + self.url)
        for div, h3 in self.__gen_div_date_list__():
            yield from self.__gen_dicts_from_div_date_list__(div, h3)

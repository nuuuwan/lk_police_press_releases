import re
from datetime import datetime
from typing import Generator

from utils import WWW, Log, Parse

log = Log("PolicePressReleasePage")


class PolicePressReleasePage(WWW):

    def __gen_div_date_list__(self):
        soup = None
        try:
            soup = self.soup
        except Exception as e:
            log.error(f"[{self}] {e}")
        if not soup:
            return

        div_list = soup.find_all(
            "div",
            attrs={"data-element_type": "container"},
        )
        for div in div_list:
            h3_list = div.find_all("h3", class_="elementor-icon-box-title")
            if len(h3_list) != 1:
                continue
            yield div, h3_list[0]

    def __get_labelled_page__(self, label):
        soup = None
        try:
            soup = self.soup
        except Exception as e:
            log.error(f"[{self}] {e}")
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

    @staticmethod
    def __parse_time_str__(x: str) -> str:
        x = x.replace("hrs.", "").replace("hrs", "").strip()

        # Handle compact 24-hour times like "2026.08.01 000" or "2026.08.01 120"
        m = re.match(r"^(\d{4})[-.](\d{2})[-.](\d{2})\s+(\d{1,2})(\d{2})$", x)
        if m:
            year, month, day, hour, minute = m.groups()
            dt = datetime(
                int(year), int(month), int(day), int(hour), int(minute)
            )
            return dt.strftime(Parse.TIME_FORMAT)

        # Handle dot-separated times like "2026.08.01 12.30"
        m = re.match(
            r"^(\d{4})[-.](\d{2})[-.](\d{2})\s+(\d{1,2})\.(\d{2})$", x
        )
        if m:
            year, month, day, hour, minute = m.groups()
            dt = datetime(
                int(year), int(month), int(day), int(hour), int(minute)
            )
            return dt.strftime(Parse.TIME_FORMAT)
        x = x.split("(")[0].strip()
        return Parse.time_str(x)

    def __gen_dicts_from_div_date_list__(
        self, div, h3
    ) -> Generator[dict, None, None]:
        date_str = h3.get_text(strip=True)
        h5_list = div.find_all("h5")
        for h5 in h5_list:
            time_str_raw = h5.get_text(strip=True)
            time_str = PolicePressReleasePage.__parse_time_str__(
                f"{date_str} {time_str_raw}"
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
        log.debug(f"Parsing {self}.")
        for div, h3 in self.__gen_div_date_list__():
            yield from self.__gen_dicts_from_div_date_list__(div, h3)

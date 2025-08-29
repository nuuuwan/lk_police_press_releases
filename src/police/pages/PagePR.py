from dataclasses import dataclass

from utils_future import Parse, WebPage


@dataclass
class PressRelease:
    time: str
    url_pdf: str


class PagePR(WebPage):
    def get_pr_list(self) -> list[PressRelease]:
        div_list = self.soup.find_all(
            "div",
            attrs={"data-element_type": "container"},
        )
        pr_list = []
        for div in div_list:
            h3_list = div.find_all("h3", class_="elementor-icon-box-title")
            if len(h3_list) != 1:
                continue
            h3 = h3_list[0]
            date_str = h3.get_text(strip=True)

            h5_list = div.find_all("h5")
            for h5 in h5_list:
                time_str = h5.get_text(strip=True)
                time = Parse.time(f"{date_str} {time_str}")

                a = h5.find("a")
                url_pdf = a["href"]
                assert url_pdf.lower().endswith(".pdf")
                pr = PressRelease(time=time, url_pdf=url_pdf)
                print(pr)
                pr_list.append(pr)
        idx = {pr.time: pr for pr in pr_list}
        pr_list = list(idx.values())
        pr_list.sort(key=lambda pr: pr.time)
        return pr_list

from utils import File, Log

log = Log("ReadMe")


class Markdown:
    @staticmethod
    def link(url: str, label: str = None) -> str:
        label = label or url
        return f"[{label}]({url})"


class ReadMe:
    PATH = "README.md"

    @property
    def lines(self):
        return [
            "# Police Documents - 🇱🇰 #SriLanka",
            "",
            "Public Documents scraped from "
            + Markdown.link("https://www.police.lk"),
            "",
        ]

    def build(self):
        File(self.PATH).write_lines(self.lines)
        log.info(f"Wrote {self.PATH}")

from utils import File, Log

from police import PressRelease

log = Log("ReadMe")


class Markdown:
    @staticmethod
    def link(url: str, label: str = None) -> str:
        label = label or url
        return f"[{label}]({url})"

    @staticmethod
    def table(d_list: list[dict]) -> list[str]:
        if not d_list:
            return []

        # Create table header
        header = " | ".join(f"{key}" for key in d_list[0].keys())
        separator = "|".join("---:" for _ in d_list[0].keys())

        # Create table rows
        rows = [" | ".join(f"{value}" for value in d.values()) for d in d_list]

        return [header, separator] + rows


class ReadMe:
    PATH = "README.md"

    @property
    def lines_status(self):
        return (
            [
                "## Scrape Status",
                "",
            ]
            + Markdown.table([PressRelease.get_aggregated_status()])
            + [""]
        )

    @property
    def lines(self):
        return [
            "# Police Documents - 🇱🇰 #SriLanka",
            "",
            "Public Documents scraped from "
            + Markdown.link("https://www.police.lk"),
            "",
        ] + self.lines_status

    def build(self):
        File(self.PATH).write_lines(self.lines)
        log.info(f"Wrote {self.PATH}")

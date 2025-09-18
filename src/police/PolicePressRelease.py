from dataclasses import dataclass
from typing import Generator

from utils import Log

from police.PolicePressReleaseHomePage import PolicePressReleaseHomePage
from scraper import AbstractPDFDoc

log = Log("PolicePressRelease")


@dataclass
class PolicePressRelease(AbstractPDFDoc):
    time_str: str

    LANG = "si"

    @classmethod
    def gen_docs(cls) -> Generator["PolicePressRelease", None, None]:
        home_page = PolicePressReleaseHomePage()
        for d in home_page.gen_dicts():
            time_str = d["time_str"]
            yield cls(
                num=time_str,
                date_str=time_str[:10],
                description=time_str,
                url_metadata=d["url_metadata"],
                lang=PolicePressRelease.LANG,
                url_pdf=d["url_pdf"],
                time_str=time_str,
            )

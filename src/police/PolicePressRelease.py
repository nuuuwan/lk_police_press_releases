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
    def get_doc_class_description(cls) -> str:
        return "\n\n".join(
            [
                "A police press release is an official public statement issued by the police to inform citizens and the media about incidents, investigations, arrests, public safety alerts, or law enforcement initiatives. It serves as an authoritative source of information, countering rumors and ensuring transparency in policing.",  # noqa: E501
                "In Sri Lanka, police press releases are especially relevant because they provide timely updates on security matters, traffic advisories, crime prevention campaigns, and major national events. Given the country’s sensitivity to issues of law, order, and public trust, these releases play a key role in shaping public awareness and confidence in the justice system.",  # noqa: E501
            ]
        )

    @classmethod
    def get_doc_class_emoji(cls) -> str:
        return "👮‍♂️"

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

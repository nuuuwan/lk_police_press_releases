import os
from dataclasses import dataclass
from functools import cached_property

from utils import JSONFile, Log

log = Log("PressRelease")


@dataclass
class PressRelease:
    time: str
    url_pdf: str

    DIR_DATA = os.path.join("..", "lk_police_docs_data", "data")

    def to_dict(self):
        return dict(
            press_release_id=self.press_release_id,
            time=self.time,
            url_pdf=self.url_pdf,
        )

    @cached_property
    def press_release_id(self):
        return self.time.replace(" ", "-").replace(":", "-")

    @staticmethod
    def __get_path_for_month__(time):
        year = time[:4]
        month = time[:7]
        return os.path.join(PressRelease.DIR_DATA, year, month)

    @cached_property
    def dir_press_release(self):
        return os.path.join(
            PressRelease.__get_path_for_month__(self.time),
            self.press_release_id,
        )

    @cached_property
    def metadata_path(self):
        return os.path.join(self.dir_press_release, "metadata.json")

    def write(self):
        os.makedirs(self.dir_press_release, exist_ok=True)
        if os.path.exists(self.metadata_path):
            return

        JSONFile(self.metadata_path).write(self.to_dict())
        log.info(f"Wrote {self.metadata_path}")

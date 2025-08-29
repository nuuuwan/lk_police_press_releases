import os
from functools import cached_property

from utils import JSONFile, Log

log = Log("PressReleaseWriteMixin")


class PressReleaseWriteMixin:
    DIR_DATA = os.path.join("..", "lk_police_docs_data", "data")

    @staticmethod
    def __get_path_for_month__(time):
        year = time[:4]
        month = time[:7]
        return os.path.join(PressReleaseWriteMixin.DIR_DATA, year, month)

    @cached_property
    def dir_press_release(self):
        return os.path.join(
            PressReleaseWriteMixin.__get_path_for_month__(self.time),
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

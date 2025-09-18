from pathlib import Path

from utils import JSONFile, Log

from police.core.press_release.PressReleaseWriteMixin import \
    PressReleaseWriteMixin

log = Log("PressReleaseReadMixin")


class PressReleaseReadMixin:

    @classmethod
    def from_dict(cls, d):
        return cls(
            time=d["time"],
            url_pdf=d["url_pdf"],
        )

    @classmethod
    def from_metadata_file(cls, metadata_path):
        d = JSONFile(metadata_path).read()
        return cls.from_dict(d)

    @staticmethod
    def __get_metadata_path_list__():
        root = Path(PressReleaseWriteMixin.DIR_DATA)
        return [str(p) for p in root.rglob("metadata.json")]

    @classmethod
    def list_all(cls):
        metadata_path_list = (
            PressReleaseReadMixin.__get_metadata_path_list__()
        )
        press_release_list = [
            cls.from_metadata_file(p) for p in metadata_path_list
        ]
        log.debug(f"Found {len(press_release_list):,} press releases.")
        return press_release_list

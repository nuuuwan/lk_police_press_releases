from dataclasses import dataclass
from functools import cached_property

from utils import Log

from police.core.press_release.PressReleaseReadMixin import \
    PressReleaseReadMixin
from police.core.press_release.PressReleaseStatusMixin import \
    PressReleaseStatusMixin
from police.core.press_release.PressReleaseWriteMixin import \
    PressReleaseWriteMixin

log = Log("PressRelease")


@dataclass
class PressRelease(
    PressReleaseWriteMixin, PressReleaseReadMixin, PressReleaseStatusMixin
):
    time: str
    url_pdf: str

    def to_dict(self):
        return dict(
            press_release_id=self.press_release_id,
            time=self.time,
            url_pdf=self.url_pdf,
        )

    @cached_property
    def press_release_id(self):
        return self.time.replace(" ", "-").replace(":", "-")

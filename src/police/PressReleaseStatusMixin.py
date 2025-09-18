from functools import cache

from utils_future import FileOrDirFuture


class PressReleaseStatusMixin:

    @classmethod
    @cache
    def get_aggregated_status(cls):
        press_release_list = cls.list_all()
        n_metadata = sum(1 for pr in press_release_list if pr.has_metadata)
        n_pdf = sum(1 for pr in press_release_list if pr.has_pdf)
        n_block_text = sum(
            1 for pr in press_release_list if pr.has_block_text
        )
        return dict(
            data=FileOrDirFuture(cls.DIR_DATA).size_humanized,
            n=len(press_release_list),
            n_metadata=n_metadata,
            n_pdf=n_pdf,
            n_block_text=n_block_text,
        )

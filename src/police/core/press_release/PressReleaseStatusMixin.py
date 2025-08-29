from functools import cache


class PressReleaseStatusMixin:

    @classmethod
    @cache
    def get_aggregated_status(cls):
        press_release_list = cls.list_all()
        n_metadata = sum(1 for pr in press_release_list if pr.has_metadata)
        n_pdf = sum(1 for pr in press_release_list if pr.has_pdf)
        return dict(
            n=len(press_release_list),
            n_metadata=n_metadata,
            n_pdf=n_pdf,
        )

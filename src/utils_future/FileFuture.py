import os
from functools import cached_property

from utils import File


class FileFuture(File):
    @cached_property
    def exists(self):
        return os.path.exists(self.path)

    @cached_property
    def size_humanized(self):
        for label, log_unit in [
            ("G", 9),
            ("M", 6),
            ("K", 3),
        ]:
            unit = 10**log_unit
            if self.size > unit:
                return f"{self.size / unit:,.1f} {label}B"
        return f"{self.size:,} B"

    @cached_property
    def size(self):
        return os.path.getsize(self.path)

    def __str__(self):
        return f"{self.path} ({self.size_humanized})"

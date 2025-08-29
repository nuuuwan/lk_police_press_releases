import os
from functools import cache, cached_property

from utils import File


class FileOrDirFuture(File):
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

    @staticmethod
    @cache
    def __get_dir_size__(path: str) -> int:
        total = 0
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):  # skip broken symlinks etc.
                    total += os.path.getsize(fp)
        return total

    @cached_property
    def size(self):
        if not self.exists:
            return 0
        if os.path.isdir(self.path):
            return self.__get_dir_size__(self.path)
        return os.path.getsize(self.path)

    def __str__(self):
        return f"{self.path} ({self.size_humanized})"

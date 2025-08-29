import sys

from police import PagePressHome

DEFAULT_MAX_DT = 120


def main(max_dt):
    max_dt = max_dt or DEFAULT_MAX_DT
    PagePressHome().spider(max_dt)


if __name__ == "__main__":
    main(max_dt=int(sys.argv[1]) if len(sys.argv) > 1 else None)

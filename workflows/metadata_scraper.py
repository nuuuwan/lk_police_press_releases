import sys

from police import PolicePressReleaseHomePage

DEFAULT_MAX_DT = 1_200


def main(max_dt):
    max_dt = max_dt or DEFAULT_MAX_DT
    PolicePressReleaseHomePage().spider(max_dt)


if __name__ == "__main__":
    main(max_dt=int(sys.argv[1]) if len(sys.argv) > 1 else None)

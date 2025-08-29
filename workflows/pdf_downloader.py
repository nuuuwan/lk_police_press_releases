import sys
import time

from utils import Log

from police import PressRelease

log = Log("pdf_downloader")


def main(max_dt):
    press_release_list = PressRelease.list_all()
    t_start = time.time()

    for press_release in press_release_list:
        dt = time.time() - t_start
        if dt > max_dt:
            log.info(f"🛑 Reached {dt:.1f} s> {max_dt}s. Stopping.")
            break
        press_release.download_pdf()
        press_release.extract_text()
    log.info("🛑 Finished downloading all PDFs.")


if __name__ == "__main__":
    main(max_dt=int(sys.argv[1]) if len(sys.argv) > 1 else None)

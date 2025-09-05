import unittest

from police import PagePressHome


class TestCase(unittest.TestCase):
    def test_get_latest_pr_page(self):
        self.assertGreater(
            PagePressHome().get_latest_pr_page().url,
            "https://www.police.lk/?p=11837",
        )

    def test_spider(self):
        max_dt = 1
        press_release_list = PagePressHome().spider(max_dt)
        self.assertGreaterEqual(len(press_release_list), max_dt)

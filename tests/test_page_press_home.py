import unittest

from police import PagePressHome


class TestCase(unittest.TestCase):
    def test_get_latest_pr_page(self):
        self.assertEqual(
            PagePressHome().get_latest_pr_page().url,
            "https://www.police.lk/?p=11837",
        )

    def test_spider(self):
        limit = 100
        pr_list = PagePressHome().spider(limit)
        self.assertGreaterEqual(len(pr_list), limit)

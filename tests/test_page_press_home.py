import unittest

from police import PagePressHome


class TestCase(unittest.TestCase):
    def test_get_latest_pr_page(self):
        self.assertEqual(
            PagePressHome().get_latest_pr_page().url,
            "https://www.police.lk/?p=11837",
        )

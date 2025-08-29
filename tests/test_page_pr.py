import unittest

from police import PagePR

TEST_URL = "https://www.police.lk/?p=11345"
TEST_PAGE_PR = PagePR(TEST_URL)


class TestCase(unittest.TestCase):
    def test_get_pr_list(self):
        pr_list = TEST_PAGE_PR.get_pr_list()
        self.assertEqual(len(pr_list), 83)

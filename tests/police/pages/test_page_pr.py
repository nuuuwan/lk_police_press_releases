import unittest

from police import PolicePressReleasePage

TEST_URL = "https://www.police.lk/?p=8986"
TEST_PAGE_PR = PolicePressReleasePage(TEST_URL)


class TestCase(unittest.TestCase):
    def test_get_press_release_list(self):
        press_release_list = TEST_PAGE_PR.get_press_release_list()
        self.assertEqual(len(press_release_list), 58)

    def test_get_more_page(self):
        more_page = TEST_PAGE_PR.get_more_page()
        self.assertEqual(more_page.url, "https://www.police.lk/?p=9733")

    def test_get_previous_page(self):
        prev_page = TEST_PAGE_PR.get_prev_page()
        self.assertEqual(prev_page.url, "https://www.police.lk/?p=8158")

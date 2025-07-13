import unittest

from utils_future import WebPage

TEST_URL = 'https://www.police.lk/?p=9472'
TEST_WEB_PAGE = WebPage(TEST_URL)


class TestCase(unittest.TestCase):
    def test_base_url(self):
        self.assertEqual(TEST_WEB_PAGE.base_url, 'https://www.police.lk')

    def test_gen_neighbours(self):
        for page in TEST_WEB_PAGE.gen_neighbours():
            self.assertIsInstance(page, WebPage)
            self.assertTrue(
                page.url.startswith('http') or page.url.startswith('/')
            )

    def test_gen_pdfs(self):
        for pdf_page in TEST_WEB_PAGE.gen_pdfs():
            self.assertIsInstance(pdf_page, WebPage)
            self.assertTrue(pdf_page.url.endswith('.pdf'))

    def test_gen_pdfs_recursive(self):
        pdf_page_list = []
        for pdf_page in TEST_WEB_PAGE.gen_pdfs_recursive():
            self.assertIsInstance(pdf_page, WebPage)
            self.assertTrue(pdf_page.url.endswith('.pdf'))
            pdf_page_list.append(pdf_page)
            if len(pdf_page_list) >= 10:
                break

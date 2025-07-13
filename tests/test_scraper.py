import unittest

from lk_police_docs import Scraper


class TestCase(unittest.TestCase):
    def test_run(self):
        Scraper(max_delta_t=1).run()

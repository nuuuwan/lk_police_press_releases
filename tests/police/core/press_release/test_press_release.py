import unittest

from police import PressRelease


class TestCase(unittest.TestCase):
    def test_list_all(self):
        press_release_list = PressRelease.list_all()
        self.assertGreaterEqual(len(press_release_list), 0)

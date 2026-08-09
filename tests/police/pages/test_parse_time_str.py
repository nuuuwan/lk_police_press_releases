import unittest

from police import PolicePressReleasePage


class TestParseTimeStr(unittest.TestCase):
    def test_compact_24h_time(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 000"),
            "2026-08-01 00:00",
        )

    def test_compact_24h_time_with_minutes(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 001"),
            "2026-08-01 00:01",
        )

    def test_compact_24h_time_three_digits(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 120"),
            "2026-08-01 01:20",
        )

    def test_dot_separated_time(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 12.30"),
            "2026-08-01 12:30",
        )

    def test_dot_separated_time_with_hrs(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 12.30 hrs."),
            "2026-08-01 12:30",
        )

    def test_colon_time(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026.08.01 12:30"),
            "2026-08-01 12:30",
        )

    def test_dash_date(self):
        self.assertEqual(
            PolicePressReleasePage.__parse_time_str__("2026-08-01 00:00"),
            "2026-08-01 00:00",
        )

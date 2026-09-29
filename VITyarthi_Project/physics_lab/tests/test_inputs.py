import unittest
from unittest.mock import patch
from helpers.inputs import ask_number


class AskNumberTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["abc", "", "5"])
    def test_skips_text(self, fake):
        self.assertEqual(ask_number("x: "), 5.0)

    @patch("builtins.input", side_effect=["-3", "0", "2"])
    def test_skips_zero_and_negative(self, fake):
        self.assertEqual(ask_number("x: "), 2.0)

    @patch("builtins.input", side_effect=["nan", "inf", "7"])
    def test_skips_nan_and_inf(self, fake):
        self.assertEqual(ask_number("x: "), 7.0)

    @patch("builtins.input", side_effect=["100", "90"])
    def test_upper_limit(self, fake):
        self.assertEqual(ask_number("x: ", high=90), 90.0)

    @patch("builtins.input", side_effect=["0"])
    def test_zero_allowed(self, fake):
        self.assertEqual(ask_number("x: ", allow_low=True), 0.0)


if __name__ == "__main__":
    unittest.main()

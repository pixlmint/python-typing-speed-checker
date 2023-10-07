import unittest
import main


class TestType(unittest.TestCase):
    def test_get_poem_lines(self):
        lines = main.get_poem_lines(2)
        self.assertIsInstance(lines, list)
        self.assertIs(2, len(lines))

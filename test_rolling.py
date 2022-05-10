import unittest
import rolling


class MyTestCase(unittest.TestCase):
    def test_highest_rolls(self):
        rolling.random.seed(1)
        self.assertEqual(rolling.highest_rolls(), [2, 5, 1])

    def test_roll_stats(self):
        rolling.random.seed(1)
        self.assertEqual(rolling.roll_stats(), [14, 12, 12, 12, 11, 14])

    def test_modifier(self):
        self.assertEqual(rolling.modifier(20), 5)
        self.assertEqual(rolling.modifier(10), 0)
        self.assertEqual(rolling.modifier(8), -1)


if __name__ == '__main__':
    unittest.main()

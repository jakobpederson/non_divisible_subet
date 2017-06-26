import non_divisible_subset
import unittest


class NonDivisibleSubsetTest(unittest.TestCase):

    def setUp(self):
        self.client = non_divisible_subset.NonDivisibleSubset()

    def test_get_subset_returns_correct_value(self):
        self.assertEqual(3,  self.client.get_subset(4, 3, [1, 7, 2, 4]))
        self.assertEqual(5, self.client.get_subset(5, 5, [2, 7, 12, 17, 22]))
        self.assertEqual(
            5, self.client.get_subset(6, 9, [422346306, 940894801, 696810740, 862741861, 85835055, 313720373])
        )
        with open('test_data.txt') as f:
            lines = [int(x) for x in f.read().strip().split(' ')]
        self.assertEqual(49747, self.client.get_subset(100000, 100, lines))

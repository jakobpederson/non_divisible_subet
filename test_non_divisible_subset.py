import non_divisible_subset
import unittest


class NonDivisibleSubsetTest(unittest.TestCase):

    def setUp(self):
        self.client = non_divisible_subset.NonDivisbileSubset()

    def test_x(self):
        n = 4
        k = 3
        arr = [1, 7, 2, 4]
        result = self.client.get_subset(n, k, arr)
        self.assertEqual(3, result)
        self.fail(self.client.get_subset(n, k, arr))

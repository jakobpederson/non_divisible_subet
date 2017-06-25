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
        n2 = 5
        k2 = 5
        arr2 = [2, 7, 12, 17, 22]
        result = self.client.get_subset(n2, k2, arr2)
        self.assertEqual(5, result)

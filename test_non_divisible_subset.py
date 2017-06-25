import non_divisible_subset
import unittest


class NonDivisibleSubsetTest(unittest.TestCase):

    def setUp(self):
        self.client = non_divisible_subset.NonDivisbileSubset()

    def test_x(self):
        self.fail(self.client.get_subset())

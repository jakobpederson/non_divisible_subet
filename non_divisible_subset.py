from itertools import combinations


class NonDivisibleSubset():

    def get_subset(self, n, k, arr):
        if k == 1:
            yield 1
        while(n > 1):
            subsets = combinations(arr, n)
            if [
                subset for subset in subsets
                if all((x + y) % k != 0 for (x, y) in combinations(subset, 2))
            ]:
                yield n
            n = n - 1
        yield 0

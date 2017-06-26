from itertools import combinations


class NonDivisbileSubset():

    def get_subset(self, n, k, arr):
        while(n > 1):
            comb = combinations(arr, n)
            for comb_ in comb:
                print(list(combinations(comb_, 2)))
                if all((x + y) % k for (x, y) in combinations(comb_, 2)):
                    return n
            n = n - 1
        return 0

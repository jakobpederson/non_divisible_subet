from itertools import combinations


class NonDivisibleSubset():

    def get_subset(self, n, k, arr):
        data = [x % k for x in arr]
        return sum([(max(data.count(i), data.count(k - i)) if i != 0 and i * 2 != k else min(1, data.count(i))) for i in range(int(k/2) + 1)])

        # for i in range(int(k/2) + 1):
        #     print(i)
        #     if i != 0 and i * 2 != k:
        #         count += max(data.count(i), data.count(k - i))
        #         print(count)
        #     else:
        #         count += min(1, data.count(i))
        # return count

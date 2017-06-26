

class NonDivisibleSubset():

    def get_subset(self, n, k, arr):
        data = [x % k for x in arr]
        return sum(self.subset_size(k, data))

    def subset_size(self, k, data):
        return [
            (
                max(data.count(i), data.count(k - i)) if i != 0 and i * 2 != k else
                min(1, data.count(i))
            )
            for i in range(int(k/2) + 1)
        ]

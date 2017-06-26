

class NonDivisbileSubset():

    def get_subset(self, n, k, arr):
        # result = set([(x, arr) for i, x in enumerate(arr) if i + 1 < len(arr) and (x + arr[i + 1]) / k != 0])
        print(k)
        result = set([x for x in arr for y in arr if x != y and (x + y) % k != 0])
        print(result)
        return(
            len(
                    result
            )
        )

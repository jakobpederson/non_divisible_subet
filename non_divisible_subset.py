

class NonDivisbileSubset():

    def get_subset(self, n, k, arr):
        # result = [x + y for i, x in enumerate(arr) for j, y in enumerate(arr) if (x + y) != 0 and i < j]
        result = set([x + y for i, x in enumerate(arr) for j, y in enumerate(arr) if i < j and (x + y) % k != 0])

        # result = set([x + y for x in arr for y in arr if (x + y) % k != 0 and x != y])
        print(result)
        return(
            len(
                    result
                    # [x + y for x in arr for y in arr if (x + y) % k != 0 and x != y]
            )
        )

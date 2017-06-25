

class NonDivisbileSubset():

    def get_subset(self, n, k, arr):
        new_arr = set(arr)
        return(
            len(
                set(
                    [x + y for x in arr for y in new_arr if (x + y) % k != 0 and x != y]
                )
            )
        )

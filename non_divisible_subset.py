from itertools import combinations


class NonDivisbileSubset():

    def get_subset(self, n, k, arr):
        result = [x for x in arr for y in arr if x != y and (x + y) % k != 0]
        print(set(result), k)

        new_result = [(x, arr[i], (x + arr[i]) % k) for i, x in enumerate(result) if i < n if (x + arr[i]) % k != 0]
        print('new', new_result)
        return(len(new_result))

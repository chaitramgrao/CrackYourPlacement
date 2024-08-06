from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        perms_unique = set(permutations(arr))
        ans = sorted(list(perms_unique))
        return ans

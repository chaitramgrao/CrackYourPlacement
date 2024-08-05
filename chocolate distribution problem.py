class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        res = float('inf')
        M -= 1
        index = 0
        while M < N:
            res = min(res, A[M] - A[index])
            index += 1
            M += 1
        
        return res

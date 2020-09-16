"""
problem can be reformulated as counting inversion in binary array
create a prefix sum and then loop through array, counting number
of 1 in A[i+1...n] for index i such that A[i] is 0
runtime complexity: O(n)
"""


def solution(A):
    n = len(A)
    pfx = [0] * (n + 1)
    for i in range(1, n + 1):
        pfx[i] = pfx[i - 1] + A[i - 1]
    ans = 0
    for i in range(1, n):
        if A[i - 1] == 0:
            ans += pfx[n] - pfx[i]
            if ans > 10 ** 9:
                return -1
    return ans

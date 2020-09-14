"""
given an array A of length n, find indexes 0 <= i<= j <= n
such that absolute sum of A[i] and A[j] is minimum
sort the array by magnitude of elements (keep track of sign)
and then check the absolute sum of consecutive element
runtime complexity: O(nlog(n))
"""


def solution(A):
    n = len(A)
    xx = []
    for item in A:
        if item >= 0:
            xx.append((item, 1))
        else:
            xx.append((abs(item), -1))
    xx.sort()
    ans = abs(2 * xx[0][0])
    for i in range(1, n):
        ans = min(ans, abs(xx[i][0] * xx[i][1] + xx[i - 1][0] * xx[i - 1][1]))
        ans = min(ans, abs(2 * xx[i][0]))
    return ans

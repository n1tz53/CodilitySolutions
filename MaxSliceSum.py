"""
given an array A find the sub-array with maximum sum
let dp[i] be the maximum sum such that sub-array ends
at ith position, then dp[i] = max(A[i], dp[i - 1] + A[i])
runtime complexity: O(len(A))
"""


def solution(A):
    n = len(A)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(A[i - 1] + dp[i - 1], A[i - 1])
    return max(dp[1:])

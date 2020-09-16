"""
shift each element of given array to right by K position
runtime complexity: O(n)
"""


def solution(A, K):
    n = len(A)
    res = [0] * n
    for i in range(n):
        res[(i + K) % n] = A[i]
    return res

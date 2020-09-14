"""
given an array A find two index i, j such that A[j] - A[i] is maximum
maintain an array mnm[0..len(A)] such that mnm[i] = min(A[0],..,A[i])
then answer would be max(A[0] - mnm[0],.....,A[len(A) - 1] - mnm[len(A) - 1])
runtime complexity: O(len(A))
"""


def solution(A):
    if len(A) < 2:
        return 0
    mnm = [0] * (len(A))
    mnm[0] = A[0]
    profit = 0
    for i in range(1, len(A)):
        mnm[i] = min(A[i], mnm[i - 1])
        profit = max(profit, A[i] - mnm[i])
    return profit

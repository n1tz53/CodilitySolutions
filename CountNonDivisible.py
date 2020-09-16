"""
given an array A of size n, for each element A[i] of A
find the # of element which doesn't divide A[i], find
the factorization of A[i] using standard approach and
check how many of these factor appears in A and with
what frequency, then answer of A[i] would be
n - 1 - # factors appearing in A
runtime complexity: O(n * sqrt(n))
"""


def solution(A):
    n = len(A)
    maxn = max(A)
    if n == 1:
        return [0]
    count = [0] * (maxn + 1)
    divs = [0] * (maxn + 1)
    for item in A:
        count[item] += 1
    divs[1] += count[1] - 1
    for idx in range(2, maxn + 1):
        if count[idx] != 0:
            j, m = 2, idx
            divs[idx] += count[1]
            divs[idx] += (count[idx] - 1)
            while j * j < m:
                if m % j == 0:
                    divs[idx] += (count[j] + count[m // j])
                j += 1
            if m == j * j:
                divs[idx] += count[j]
    result = [0] * len(A)
    for i in range(n):
        result[i] = n - 1 - divs[A[i]]
    return result

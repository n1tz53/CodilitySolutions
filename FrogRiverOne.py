"""
given an array A of length n and an integer x find the minimum index idx such that A[0..idx]
contains all integer from 1 to x, maintain array mark[1..X] and counter,
loop over A and set mark[A[i]] = True if its false and increase counter by one,
return when counter equals X
runtime complexity: O(n)
"""


def solution(X, A):
    n = len(A)
    mark = [False] * X
    count = 0
    for (idx, item) in enumerate(A):
        if not mark[item - 1]:
            mark[item - 1] = True
            count += 1
            if count == X:
                return idx
    return -1

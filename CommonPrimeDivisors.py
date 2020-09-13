"""
let d = gcd(a, b)
d contains common prime factors of a and b
remove common prime factors with their powers
from prime factorisation a and b, if a and b
reduce to 1 it means they have same prime factors
"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solution(A, B):
    n = len(A)
    ans = 0
    for i in range(n):
        d = gcd(A[i], B[i])
        a = A[i] // d
        b = B[i] // d
        da = gcd(d, a)
        db = gcd(d, b)
        while not (da == 1 or a == 1):
            # remove common factor of a and d, from a
            a /= da
            da = gcd(d, a)
        while not (db == 1 or b == 1):
            # remove common factor of b and d, from b
            b /= db
            db = gcd(b, d)
        if a == 1 and b == 1:
            ans += 1
    return ans

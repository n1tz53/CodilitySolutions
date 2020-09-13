"""
if x and y have same prime factors then gcd, d of x and y will have those
prime factors as well, to remove those common prime factors from x and y take gcd,
da of d and x and keep diving x with da until da is 1 or x is 1, repeat similar
procedure for y, both x and y should reduce to 1 if they have same prime factors
"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solution(A, B):
    n = len(A)
    ans = 0
    for i in range(n):
        if A[i] == B[i]:
            ans += 1
            continue
        d = gcd(A[i], B[i])
        if d != 1:
            a = A[i] // d
            b = B[i] // d
            while True:
                da = gcd(a, d)
                if da == 1 or a == 1:
                    break
                a /= da
            while True:
                db = gcd(b, d)
                if db == 1 or b == 1:
                    break
                b /= db
            if a == 1 and b == 1:
                ans += 1
    return ans

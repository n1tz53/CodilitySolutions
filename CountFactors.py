"""
count number of divisors of N
if N = p1^e1 * p2^e2 ... * pk^ek
is prime factorization of N,
then # of divisors are (e1 + 1) * (e2 + 1) * .... * (ek + 1)
runtime complexity: O(sqrt(N))
"""

def solution(N):
    ans = 1
    fac = 2
    while fac * fac <= N:
        e = 0
        while N % fac == 0:
            e += 1
            N = N // fac
        ans = ans * (e + 1)
        fac += 1
    if N > 1:
        ans = ans * 2
    return ans
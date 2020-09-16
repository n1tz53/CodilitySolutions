"""
need to find semi-prime between 1 to N,
calculate all prime between 1 to N using sieve of Eratosthenes,
then calculate all semi prime in O(N * sqrt(N)) times
runtime complexity: O(N * sqrt(N))
"""


def sieve_erato(n):
    prime = [True] * (n)
    prime[0] = False
    prime[1] = False
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
        i += 1
    primes = []
    for i in range(2, n):
        if prime[i]:
            primes.append(i)
    return primes


def solution(N, P, Q):
    # handle corner case
    if N < 4:
        return [0] * len(P)
    primes = sieve_erato(N + 1)
    semiprime = [0] * (N + 1)
    p = 0
    while primes[p] * primes[p] <= N:
        for q in range(p, len(primes)):
            if primes[p] * primes[q] <= N:
                semiprime[primes[p] * primes[q]] = 1
            else:
                break
        p += 1
    pfx = [0] * (N + 1)
    for i in range(1, N + 1):
        pfx[i] = pfx[i - 1] + semiprime[i]
    result = []
    for qry in range(len(P)):
        result.append(pfx[Q[qry]] - pfx[P[qry] - 1])
    return result

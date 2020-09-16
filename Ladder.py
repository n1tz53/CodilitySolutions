"""
calculate Fibonacci number upto L modulo 2^p
to avoid TLE pre-calculate fib(1..L) modulo 2^30
then to calculate modulo 2^q (q <= 30) use the same
runtime complexity: O(L)
"""


def solution(A, B):
    n = len(A)
    L = max(A)
    fib = [0] * (L + 1)
    fib[0], fib[1] = 1, 1
    for i in range(2, L + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << 30) - 1)
    result = []
    for i in range(n):
        result.append(fib[A[i]] & ((1 << B[i]) - 1))
    return result

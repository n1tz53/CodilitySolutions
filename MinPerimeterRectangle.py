"""
for given N find pair of divisor such that perimeter of rectangle
form by those divisor as side is minimum, divisor closest to
sqrt(N) will be the desired pair
runtime complexity: O(sqrt(N))
"""

from math import sqrt


def solution(N):
    div = int(sqrt(N)) + 1
    while N % div != 0:
        div -= 1
    return 2 * (div + N // div)

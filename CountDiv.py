"""
return the number of elements divisible by K between A and B inclusive
let x be such that K * x <= B abd y be such that k * y <= A - 1
then x - y is multiple of K between A and B
runtime complexity: O(1)
"""

from math import floor


def solution(A, B, K):
    return int(floor(B / K)) - int(floor((A - 1) / K))

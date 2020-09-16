"""
given an array containing 2*n+1 elements, such that except
one element others are duplicate pair, find the unpaired element
take xor of all elements, duplicate elements will become zero
runtime complexity: O(n)
"""


def solution(A):
    res = 0
    for item in A:
        res = res ^ item
    return res

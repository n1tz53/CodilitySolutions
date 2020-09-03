'''
check if elements from 1 to n appear
in array where n is len of array
'''

def solution(arr):
    n = len(arr)
    mark = [False] * n
    for item in arr:
        if item <= n:
            mark[item - 1] = True
    if mark.count(True) == n:
        return 1
    else:
        return 0
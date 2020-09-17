"""
observe that if you can set x flags, then you can
set 1,..,x - 1 flags to and if you can't set x flags
then you can't set x + 1, ... N as well, then perform
binary search to find max x you can set flag for
runtime complexity: O(n * ln(n))
"""


def solution(A):
    n = len(A)
    if n < 3:
        return 0
    peaks = []
    for i in range(1, n - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks.append(i)
    if len(peaks) < 3:
        return len(peaks)
    else:
        low, high = 1, len(peaks)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            flag, last, ctr = mid, 0, 1
            for i in range(1, len(peaks)):
                if peaks[i] - peaks[last] >= flag:
                    ctr += 1
                    last = i
            if flag <= ctr:
                low = mid + 1
                ans = max(ans, flag)
            else:
                high = mid - 1
        return ans

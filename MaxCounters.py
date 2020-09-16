"""
see comment for solution
runtime complexity: O(n)
"""


def solution(N, A):
    fmxc = 0
    # set N counters to 0 initialy
    counters = [0] * N
    # find largest index with value N + 1
    for i in range(len(A)):
        if A[i] == N + 1:
            fmxc = i
    last_mx = 0  # store last max value each counter will take
    cur_mx = 0  # store current max
    for i in range(fmxc + 1):
        if A[i] == N + 1:
            last_mx = cur_mx
        else:
            # if counter is less than last max value then update it
            if counters[A[i] - 1] < last_mx:
                counters[A[i] - 1] = last_mx
            counters[A[i] - 1] += 1
            cur_mx = max(counters[A[i] - 1], cur_mx)
    # if counter is less than last max value then update it
    for i in range(N):
        if counters[i] < last_mx:
            counters[i] = last_mx
    # perform increment after last global update of counters
    for i in range(fmxc + 1, len(A)):
        counters[A[i] - 1] += 1
    return counters

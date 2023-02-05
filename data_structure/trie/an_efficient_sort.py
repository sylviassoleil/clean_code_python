import array as arr
from bisect import bisect_left

def cookies(k, A):
    # Write your code here
    operations = 0
    A = arr.array('i', A)
    # new = None
    start_loc = [0, 0]
    # if len(A)>1:
    #     if (k-A[-1])/2*A[-2]>len(A):
    # soft bound
    # if A[-1]*2+A[-2]<k:
    # return -1
    while 1:
        if A[0] >= k:
            return operations
        elif len(A) == 1:
            return -1
        else:
            # min_0, min_1 = A[start_loc], A[start_loc+1]
            new = A[0] + A[1] * 2
            operations += 1
            # start_loc+=2
            del A[:2]
            ind = bisect_left(A, new)
            A.insert(ind, new)


# !/bin/python3

import math
import os
import random
import re
import sys
import array as arr


# from bisect import bisect_left

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
'''success!!!'''
# takeaways:
# long list pop is expensive
# array.array is not optimized array
# bisect is a great package (Ologn) but is dominated by insert index O(n)
# better to append to the list (if we know the list is going up) and use index
# !!!!
def get_mins(a, n, start_loc):
    l = a[start_loc[0]:start_loc[0] + 2] + n[start_loc[1]:start_loc[1] + 2]
    l = sorted(l)
    min_0 = l[0]
    min_1 = None

    if len(l) > 1:
        min_1 = l[1]
        if (l[0] in a[start_loc[0]:start_loc[0] + 2]):
            start_loc[0] += 1
        else:
            start_loc[1] += 1
        if (l[1] in a[start_loc[0]:start_loc[0] + 2]):
            start_loc[0] += 1
        else:
            start_loc[1] += 1

    return min_0, min_1


def cookies(k, A):
    # Write your code here
    operations = 0
    A = arr.array('i', sorted(A))
    N = arr.array('i')
    start_loc = [0, 0]

    while 1:
        min_0, min_1 = get_mins(A, N, start_loc)
        if min_0 >= k:
            return operations
        if min_1 is None:
            return -1
        else:
            new = min_0 + 2 * min_1
            N.append(new)
            operations += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()

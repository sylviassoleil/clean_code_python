#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# f(n) = 1*x1+2*x2...n*xn
# Z(n) = sum(f(n))
# Z(n+1) = Z(n) + x[n]*rank + sum(x_i for i>rank)

def sortedSum(a):
    # Write your code here
    mod_val = 10 ** 9 + 7
    len_a = len(a)
    sum_f = 0
    f_ = 0
    for i in range(len_a):
        j = i
        while (j > 0) & (a[j] < a[j - 1]):
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

        # j = 0
        f_ += a[j] * (j + 1) % mod_val
        j+=1
        while j <= i:
            f_ += a[j] % mod_val
            j += 1
        sum_f+=f_

    return sum_f % mod_val


def getsum(BITTree, i):
    s = 0
    i += 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

def updatebit(BITTree, n, i, v):
    # BITTREE[0] is a dummy node
    i+=1 # index in Bittree is 1 more than i in array
    while i<=n:
        BITTree[i]+=v
        i+= i&(-i) #odd&(-odd) = 1, even&(-even)=even, get the parent
        print(i)
    return BITTree

def construct(arr, n):
    BITTree = [0]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])

    return BITTree


def sortedSum(a):
    # Write your code here
    max_a = 10**6
    mod_val = 10 ** 9 + 7

    len_a = len(a)
    pre = [0]*(max_a+1)
    post = [0]*(max_a+1)
    # n_bittree = len_a+1
    f_ = a[0]
    sum_f = f_
    total_sum = f_
    # bittree = construct(sorted(a), len_a)
    pre = updatebit(pre, max_a, a[0], 1)
    post = updatebit(post, max_a, a[0], a[0])

    for i in range(1, len_a):
        rank = getsum(pre, a[i])+1
        sum_greater_than_i = total_sum-getsum(post, a[i])

        # j = 0
        f_ = (f_ + a[i] * rank+sum_greater_than_i) % mod_val
        sum_f=(sum_f+f_)% mod_val
        total_sum+=a[i]

        pre = updatebit(pre, max_a, a[i], 1)
        post = updatebit(post, max_a, a[i], a[i])

    return sum_f % mod_val


if __name__ == '__main__':
    a = [3,5,9,7]
    t = sortedSum(a)
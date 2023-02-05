#!/bin/python3

import sys


def fib(n):
    # starting from 1
    # n_1 = 1
    # n_2 = 2
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)


def even_fib(n):
    if not n:
        return 0

    return even_fib(n - 1) + fib(3 * n - 1)

def even_fib_sum(n):
    sum_ = 1
    if n<1:
        return 0
    for i in range(3*n):
        sum_ += fib(i)
    return sum_//2

def get_even_sum(N):
    n = 1
    while 1:
        fib_n = -1 + 3 * n
        fib_num = fib(fib_n)
        if fib_num > N:
            return even_fib(n - 1)
        n += 1


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_even_sum(n))
'''
Knapsack problem
Given a set of items, each with a weight and a value,
determine the number of each item to include in a collection so that
the total weight is less than or equal to a given limit and the total value is as large as possible.
0-1 knapsack
    - maximize sum of v_i*x_i, subject to sum w_i* x_i<=W, x_i in {0,1}
bounded knapsack problem
    - x_i in {0, 1, 2, ...c}

unbounded knapsack problem
    - x_i>=0 and x_i is integer
    - solution dynamic programming in-advance algo
        m[0]=0
        m[w] = max(v1+m[w-w1], v2+m[w-w2]....), w_i<=w

Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
There is a limitless supply of each coin type.

'''

import math
import re
from bisect import bisect_right
import heapq

def getWays_sucks(n, c, ways=None):
    if ways is None:
        ways = 0
    if n == 0:
        ways+= 1

    if len(c)==0:
        return 0
    elif len(c)>0:
        # print(ways)
        c.sort()
        # heapq.heapify(c)
        ind = bisect_right(c, n)
        c_working = c[:ind][::-1]

        if len(c_working) > 0:
            for i, v in enumerate(c_working):
                # print((n - v, c_working[i:],))
                # print('c', ways)
                ways = getWays(n - v, c_working[i:], ways)

        return ways

def get_ways_recursive(n, c):
    cache = {}
    c.sort()

    def dfs(i, a):
        # i index for coins
        if a == n:
            return 1
        if a > n:
            return 0
        if i == len(c):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]

        cache[(i, a)] = dfs(i, a+c[i]) + dfs(i+1, a)
        return cache[(i,a)]

    return dfs(0, 0)


def getWays(n, c):
    dp = [0]*(n+1)
    dp[0] = 1
    c.sort()
    # c = c[:bisect_right(c, n)]
    # m = len(c)
    for i in c:
        if i>n:
            break
        k = i
        while k<=n:
            dp[k] +=dp[k-i]
            k+=1
        # print((i, dp[i],  dp),)
    return dp[n]

def _getWays(n, c):
    c.sort()
    # c = c[:bisect_right(c, n)]
    l_c = len(c)
    l = [[0]*(n+1)]*l_c
    for i in range(l_c):
        for j in range(n+1):
            if i==0:
                l[i][j] = 1 if j%c[i]==0 else 0
            else:
                if c[i]>j:
                    l[i][j] = l[i-1][j]
                else:
                    l[i][j] = l[i-1][j]+l[i][j-c[i]]
    return l[l_c-1][n]


if __name__ == '__main__':
    pass
    n = 75
    # c = [2, 5, 3, 6]
    c = [25, 10, 11, 29, 49, 31, 33, 39, 12, 36, 40, 22, 21, 16, 37, 8, 18, 4, 27, 17, 26, 32, 6, 38, 2, 30, 34]

    # c = [2, 5]
    w = getWays(n, c)
    w_r = get_ways_recursive(n, c)
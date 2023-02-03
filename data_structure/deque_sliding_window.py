from collections import deque

'''Given an array and an integer K, 
find the maximum for each and every contiguous subarray of size K.
'''

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
K = 3

def printMax(arr, N, K):
    Qi = deque() # length = K
    # store useful indexes

    for i in range(K):
        while Qi & (arr[i]>=arr[Qi[-1]]):
            Qi.pop()
        Qi.append(i)

    for i in range(K, N):
        print(str(arr[Qi[0]]) + " ", end="")
        while Qi & (Qi[0])<=i-K:
            Qi.popleft()
        #     pop from left

        while Qi & (arr[i]>=arr[Qi[-1]]):
            Qi.pop() #pop from right
        Qi.append(i)

        print(str(arr[Qi[0]]))

def stock_prices(prices):
    len_s = len(prices)
    if len_s < 2:
        return 0
    buy_ind = 0
    # min_inds = deque([0])
    sell_ind = 1
    # max_inds = deque([0])
    profit = prices[sell_ind]-prices[buy_ind]
    # profit = {(0, 1): prices[sell_ind]-prices[buy_ind]}
    profit = 0
    for sell_ind in range(1, len_s):
        # shift buy date
        if prices[buy_ind]<prices[sell_ind]:
            profit_ = prices[sell_ind] - prices[buy_ind]
            profit = max(profit, profit_)
        else:
            buy_ind = sell_ind

    return max(profit, 0)


if __name__ == '__main__':
    pass
    # q = deque([1,2,3])
    stocks = []
    stock_prices([])

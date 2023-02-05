# https://www.hackerrank.com/challenges/new-year-chaos/problem

def minimum_bribes(q):
    # Write your code here
    # brute force method
    len_q = len(q)
    swap = 0
    i = len_q-1
    while i!=0:
        if q[i]<i+1:
            # larger num is brought forward
            if q[i-1] == i+1:
                q[i-1], q[i] = q[i], q[i-1]
                swap += 1
            elif q[i-2] == i+1:
                q[i-2], q[i] = q[i], q[i-2]
                q[i-2], q[i-1] = q[i-1], q[i-2]
                swap += 2
            else:
                print('Too chaotic')
                return
        i -= 1
    print(swap)

if __name__ == '__main__':
    l = [1, 2, 5, 3, 7, 8, 6, 4]
    minimum_bribes(l)
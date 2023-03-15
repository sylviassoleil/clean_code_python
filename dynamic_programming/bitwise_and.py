import bisect


def countPairs(arr):
    pair = 0
    cache = set([])
    notin = set([])
    # arr = sorted(arr)
    len_arr = len(arr)
    for i in range(len_arr - 1):
        for j in range(i + 1, len_arr):
            if (frozenset((arr[i], arr[j])) in cache) or (frozenset((arr[j], arr[i])) in cache):
                pair += 1
                continue
            elif (frozenset((arr[i], arr[j])) in notin) or (frozenset((arr[j], arr[i])) in notin):
                continue
            val = arr[i] & arr[j]
            if (val != 0) and ((val) & (val - 1) == 0):
                pair += 1
                cache.add(frozenset((arr[i], arr[j])))
            else:
                notin.add(frozenset((arr[i], arr[j])))
    return pair

def countPairs(arr):
    pair = 0
    cache = {}
    # arr = sorted(arr)
    len_arr = len(arr)
    dp = [[0 for _ in range(len_arr+1)] for _ in range(len_arr+1)]
    for i in range(len_arr):
        if arr[i] in cache:
            cache[arr[i]] = cache[arr[i]]+1


def getMaxArea(w, h, isVertical, distance) -> list:
    # Write your code here
    out = []
    # xmax = 0
    # ymax = 0
    vers = [0 for _ in range(h+1)]  # heapq.heapify([])
    horis = [0 for _ in range(w+1)]  # heapq.heapify([])
    vers[0] = 1
    horis[0] = 1
    vers[h] = h
    horis[w] = w
    last = 0
    # find the biggest horizonal gap and vertical gap after each insertion
    def update_arr(d, arr):
        for i in range(d, -1, -1):
            if arr[i]>0:
                arr[d] = d-i
                break
        for i in range(d+1, len(arr)):
            if arr[i]>0:
                arr[i] = i-d
        return arr

    for v, d in zip(isVertical, distance):
        if v:
            if (vers[d]):
                out.append(last)
                continue
            # is vertical
            vers = update_arr(d, vers)

        else:
            if (horis[d]):
                out.append(last)
                continue
            print(horis)
            horis = update_arr(d, horis)

        print(vers, horis)
        last = max(vers) * max(horis)
        out.append(last)
    return out

if __name__ == '__main__':
    pass
    w=4
    h=4
    isVertical = [0,1]
    distance = [3,3]
    out = getMaxArea(w, h, isVertical, distance)







def trap_the_water(blocks):
    ''' this can be improved! '''
    # blocks = [0, 1, 2, 3, 0, 1, 2, 5, 2]
    trapped = 0
    left_max = [blocks[0]]
    right_max = [blocks[-1]]
    for ind in range(1, len(blocks)):
        left_max.append(max(blocks[ind], left_max[ind-1]))
    for ind in range(1, len(blocks)):
        right_max.append(max(blocks[-ind-1], right_max[ind-1]))
    # print(left_max)
    # print(right_max)
    for x, left, right in zip(blocks, left_max, right_max[::-1]):
        # left_max = max(left, left_max)
        # right_max = max(right, right_max)
        trapped += min(left, right) - x
    return trapped

if __name__ == '__main__':
    blocks = [0, 1, 2, 3, 0, 1, 2, 5, 2]
    print(trap_the_water(blocks))
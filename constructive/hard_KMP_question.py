def kmp(x):
    # Write your code here
    # scores = {1:0}
    # N = sum(x)
    # for i in range(2, N):
    #     l = scores[i-1]
    #     while (l>0) & (S[i]!=S[l+1]):
    #         l = scores[l]
    #
    #     if S[i] == S[l+1]:
    #         scores[i] = l+1
    #     else:
    #         scores[i] = 0


    from string import ascii_lowercase
    out = []
    min_index = 0
    for i, v in enumerate(x):
        out.append(ascii_lowercase[i] * v)
        if v < x[min_index]:
            min_index = i

    min_character = out[min_index]
    out[min_index] = ''
    return ''.join([min_character, *out])

if __name__ == '__main__':
    pass


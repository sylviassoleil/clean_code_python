def abbreviation(a, b):
    b_len = len(b)
    a_len = len(a)
    if b_len > a_len:
        return "NO"

    dp = [[False for _ in range(b_len+1)] for _ in range(a_len+1)]
    dp[0][0] = True
    for i in range(a_len):
        for j in range(b_len+1):
            if dp[i][j]:
                if (j < b_len)  & (a[i].upper() == b[j]):
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i+1][j] = True
    return  "YES" if dp[a_len][b_len] else "NO"
    #     dp[i][0] = (a[i].islower()) | (a[i].upper()==b[0])
    # for i in range(1, a_len):
    #     dp[i][0] = (dp[i][0]) & (dp[i-1][0])
    #     for k in range(1, b_len):
    #         # print(i, k)
    #         dp[i][k] = (dp[i-1][k-1] & ((a[i].upper() == b[k])|(a[i].islower()))) | (dp[i][k-1] & ((a[i].upper() == b[k])|(a[i].islower())))
    # print(dp)
    # return "YES" if dp[-1][-1] else "No"
def abbreviation(a, b):
    if len(a)<len(b):
        return "NO"

    dp = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    dp[0][0] = True
    for i in range(len(a)):
        for j in range(len(b)+1):
            if dp[i][j]:
                if j < len(b) and a[i].upper() == b[j]:
                    dp[i+1][j+1] = True
                if a[i].islower():
                    dp[i+1][j] = True
    return 'YES' if dp[len(a)][len(b)] else 'NO'


def longest_common_subsequence_bottomUp(text1, text2):
    dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

    for i in range(len(text2), -1, -1):
        for j in range(len(text1), -1, -1):
            if text2[i] == text1[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

def longest_common_subsequence(text1, text2):
    if len(text1) ==0 | len(text2)==0:
        return 0
    if text1[-1] == text2[-1]:
        return 1 + max(longest_common_subsequence(text1[:-1], text2[:-1]))
    else:
        return max(longest_common_subsequence(text1[:-1], text2), longest_common_subsequence(text1, text2[:-1]))

def maxProfit():
    
    return

if __name__ == '__main__':
    a = 'aBcde'.lower()
    b = 'ABCd'.lower()
    a = "abcde"
    b = "ace"

    # r = abbreviation(a, b)
    cs = longest_common_subsequence(a, b)
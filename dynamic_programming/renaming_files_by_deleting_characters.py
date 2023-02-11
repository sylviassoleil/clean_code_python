#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def renameFile(newName, oldName):
    '''

    :param newName: a subsequence of oldName
    :param oldName:
    :return:
    '''
    n = len(newName)
    m = len(oldName)
    dp = [1 for _ in range(m + 1)] # find with more characters included,
    for i in range(1, n + 1):
        ''' subquestion: find the possible new name in old name[i:] '''
        dpp = [0 for _ in range(m + 1)]
        for j in range(i, m + 1):
            dpp[j] = dpp[j - 1] # dpp should be at least dpp[j-1]
            if newName[i - 1] == oldName[j - 1]:
                dpp[j] += dp[j - 1] # then dp[j-1] ways should also be possible
        dp = dpp
    return dp[-1] % (10**9 + 7)
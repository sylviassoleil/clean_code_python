from string import ascii_uppercase
import numpy as np

''' inputs
longer string s: consists of all uppercase letters 
shorter string t: consists of all uppercase letters 

output
find the index of the minimum substring of the longer strings that contains all the alphabets in t, regardless of the order
i.e if 
s = 'ABCDECDF'
t = 'FD'
the minimum substring is 'DF', return corresponding index of the substring is [6:8]

if such substring does not exist, return '' 

'''

''' find the equivalent of the dictionary!'''
def find_minimum_string(s, t) -> str:
    len_s = len(s)
    len_t = len(t)
    if (len_t > len_s) or (len_t == 0):
        return ""
    characters_to_search = {}
    characters_found = {}
    res_len = float("infinity")
    for i in range(len_t):
        characters_to_search[t[i]] = characters_to_search.get(t[i], 0) + 1
    need = len(characters_to_search)
    res = [0, 0]
    have = 0
    l = 0

    for i in range(len_s):
        if (s[i] in characters_to_search):
            characters_found[s[i]] = 1 + characters_found.get(s[i], 0)
            if characters_found[s[i]] == characters_to_search[s[i]]:
                have+=1 # if more than needed will not add to count

            while have == need:
                c = s[l]
                curret_len = i-l+1
                if curret_len<res_len:
                    res = [l, i] # this is the output
                    res_len = curret_len
                if c in characters_found:
                    characters_found[c] = characters_found[c]-1 # if later another c is found, then this will be filled
                    if characters_found[c]<characters_to_search[c]:
                        have-=1
                l+=1

    l, r = res
    return s[l:r+1] if res_len!=float("infinity") else ""


if __name__ == '__main__':
    ''' input '''
    # len_t = np.random.randint(10, 200)
    # len_s = np.random.randint(len_t, 2000)
    # s = ''.join(np.random.choice(list(ascii_uppercase), len_s))
    # t = ''.join(np.random.choice(list(ascii_uppercase), len_t))
    s = t ='aa'
    s = "cabwefgewcwaefgcf"
    t = "cae"
    res = find_minimum_string(s, t)
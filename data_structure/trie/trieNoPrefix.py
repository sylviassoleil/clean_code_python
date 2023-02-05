class TrieNode:
    def __init__(self):
        # if a-j
        # from string import ascii_lowercase
        self.children = [None]*10
        self.isEnd = 0

class Trie:
    def __init__(self):
        self.root = self.getNode()
        # self.wordswPrefix = set([])

    def getNode(self):
        return TrieNode()

    def _chartToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for ind in range(length):
            index = self._chartToIndex(key[ind])
            if pCrawl.children[index] is None:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            if pCrawl.isEnd:
                print("BAD SET")
                print(key)
                return False
                # self.wordswPrefix.add(array_place)

        pCrawl.isEnd +=1
        if any([i is not None for i in pCrawl.children]):
            print("BAD SET")
            print(key)
            return False
        return True

    def search(self, word):
        pCrawl = self.root
        length = len(word)
        for i in range(length):
            index = self._chartToIndex(word[i])
            if pCrawl.children[index] is None:
                return False
            pCrawl = pCrawl.children[index]

        if pCrawl.isEnd:
            return True
        else:
            return False

    def hasPrefix(self, word):
        pCrawl = self.root
        length = len(word)
        for i in range(length):
            index = self._chartToIndex(word[i])
            if pCrawl.isEnd:
                if i<length-1:
                    return True
                else:
                    if pCrawl.isEnd>1:
                        return True
            pCrawl = pCrawl.children[index]
        return False

    def getPrefixFor(self, word):
        pCrawl = self.root
        length = len(word)
        for i in range(length):
            index = self._chartToIndex(word[i])
            pCrawl = pCrawl.children[index]
        return pCrawl.prefixFor

def noPrefix(words):
    if len(words) == 1:
        print('GOOD SET')
        return
    trie = Trie()
    for word in words:
        keep = trie.insert(word)
        if not keep:
            return

    print('GOOD SET')

def noPrefix_(words):
    head = {}
    for word in words:
        print(head)
        itr = head
        for w in word:
            if w not in itr:
                itr[w] = {}
            itr = itr[w]

            if "*" in itr:
                print("BAD SET")
                print(word)
                return
        if itr != {}:
            print("BAD SET")
            print(word)
            return
        itr["*"] = "*"
    print("GOOD SET")

if __name__ == '__main__':
    pass
    words = ['aab', 'aac', 'aacghgh', 'aabghgh',]
    words = '''100
hgiiccfchbeadgebc
biiga
edchgb
ccfdbeajaeid
ijgbeecjbj
bcfbbacfbfcfbhcbfjafibfhffac
ebechbfhfcijcjbcehbgbdgbh
ijbfifdbfifaidje
acgffegiihcddcdfjhhgadfjb
ggbdfdhaffhghbdh
dcjaichjejgheiaie
d
jeedfch
ahabicdffbedcbdeceed
fehgdfhdiffhegafaaaiijceijdgbb
beieebbjdgdhfjhj
ehg
fdhiibhcbecddgijdb
jgcgafgjjbg
c
fiedahb
bhfhjgcdbjdcjjhaebejaecdheh
gbfbbhdaecdjaebadcggbhbchfjg
jdjejjg
dbeedfdjaghbhgdhcedcj
decjacchhaciafafdgha
a
hcfibighgfggefghjh
ccgcgjgaghj
bfhjgehecgjchcgj
bjbhcjcbbhf
daheaggjgfdcjehidfaedjfccdafg
efejicdecgfieef
ciidfbibegfca
jfhcdhbagchjdadcfahdii
i
abjfjgaghbc
bddeejeeedjdcfcjcieceieaei
cijdgbddbceheaeececeeiebafgi
haejgebjfcfgjfifhihdbddbacefd
bhhjbhchdiffb
jbbdhcbgdefifhafhf
ajhdeahcjjfie
idjajdjaebfhhaacecb
bhiehhcggjai
bjjfjhiice
aif
gbbfjedbhhhjfegeeieig
fefdhdaiadefifjhedaieaefc
hgaejbhdebaacbgbgfbbcad
heghcb
eggadagajjgjgaihjdigihfhfbijbh
jadeehcciedcbjhdeca
ghgbhhjjgghgie
ibhihfaeeihdffjgddcj
hiedaegjcdai
bjcdcafgfjdejgiafdhfed
fgdgjaihdjaeefejbbijdbfabeie
aeefgiehgjbfgidcedjhfdaaeigj
bhbiaeihhdafgaciecb
igicjdajjdegbceibgebedghihihh
baeeeehcbffd
ajfbfhhecgaghgfdadbfbb
ahgaccehbgajcdfjihicihhc
bbjhih
a
cdfcdejacaicgibghgddd
afeffehfcfiefhcagg
ajhebffeh
e
hhahehjfgcj
ageaccdcbbcfidjfc
gfcjahbbhcbggadcaebae
gi
edheggceegiedghhdfgabgcd
hejdjjbfacggdccgahiai
ffgeiadgjfgecdbaebagij
dgaiahge
hdbaifh
gbhccajcdebcig
ejdcbbeiiebjcagfhjfdahbif
g
ededbjaaigdhb
ahhhcibdjhidbgefggdjebfcf
bdigjaehfchebiedajcjdh
fjehjgbdbaiifi
fbgigbdcbcgffdicfcidfdafghajc
ccajeeijhhb
gaaagfacgiddfahejhbgdfcfbfeedh
gdajaigfbjcdegeidgaccjfi
fghechfchjbaebcghfcfbdicgaic
cfhigaciaehacdjhfcgajgbhhgj
edhjdbdjccbfihiaddij
cbbhagjbcadegicgifgghai
hgdcdhieji
fbifgbhdhagch
cbgcdjea
dggjafcajhbbbaja
bejihed
eeahhcggaaidifdigcfjbficcfhjj'''
    words = words.split()[1:]
    noPrefix(words)


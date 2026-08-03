class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=(i+'\n')
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        beg = 0
        for i in range(len(s)):
            if s[i] == '\n':
                res.append(s[beg:i])
                if i != range(len(s)-1):
                    beg = i+1
        return res



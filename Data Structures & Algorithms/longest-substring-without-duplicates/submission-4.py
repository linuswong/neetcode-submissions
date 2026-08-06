class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        res  =0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l +1)
        return res






        # if(len(s)) == 0:
        #     return 0
        # count = 0
        # max = 1
        # letters = {}

        # for i in range(len(s)):
        #     if s[i] in letters:
        #         letters[s[i]].append(i)
        #     else:
        #         letters[s[i]] = [i]
        # for key, val in letters.items():
        #     for i in range(len(val)-1):
        #         calc = val[i+1] - val[i]
        #         max = calc if calc > max else max
        # return max

        # for l in s:
        #     letters[l] = letters.get(l,0)+1
            
        # for key, value in letters:

            
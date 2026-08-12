class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t =="":
            return ""
        
        countT,window = {},{}
        

        for c in t:
            countT[c] = 1+countT.get(c,0)
        
        have,need = 0, len(countT)

        res = ""
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                res = s[l:r+1] if r-l+1 < len(res) or res == "" else res

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        return res



        # if len(s) < len(t) or t =="":
        #     return ""

        # tCount = {}
        # sCount = {}

        # for c in t:
        #     tCount[c] = tCount.get(c,0)+1
        #     sCount[c] = 0
        # print(tCount)
        # print(sCount)
        
        # res = ""


        # l = 0
        # for r in range(len(s)):

        #     if s[r] in sCount:
        #         sCount[s[r]] +=1


        #     if sCount == tCount:
        #         res = s[l:r+1] if len(s[l:r+1])<len(res) or res =="" else res
        #         print("equal")
        #         print(s[l:r+1])
        #         while l != r and sCount == tCount:
        #             if s[l] in sCount:
        #                 sCount[s[l]] -= 1
        #             l+=1
        #         res = s[l-1:r+1] if len(s[l-1:r+1])<len(res) or res =="" else res
        # print(l)
        # print(r)
        # print(s[1:2])
        # if s[l] not in tCount or (s[l] in sCount and --sCount[s[l]] == tCount[s[l]]):
        #     res = s[l:r+1] if len(s[l:r+1])<len(res) or res =="" else res
        # return res

                    
            




        # if len(s)<len(t):
        #     return ""
        # sCount = {}
        # tCount = {}
        # letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # print(len(letters))

        # l=0
        # res = ""

        # matches = 0 #maxMatches = 52

        # for c in letters:
        #     sCount[c] = sCount.get(c,0)
        #     tCount[c] = tCount.get(c,0)
        # for i in range(len(t)):
        #     sCount[s[i]] += 1#sCount.get(s[i],0)+1
        #     tCount[t[i]] += 1#tCount.get(t[i],0)+1
        # for c in letters:
        #     matches += (1 if sCount[c] == tCount[c] else 0)
        
        # print(sCount,end ="\n\n")
        # print(tCount)

        # for r in range(len(t),len(s)):
        #     if matches == 52:
        #         while matches == 52:
        #             print("52 matches")
        #             print("L:" +str(l))
        #             sCount[s[l]]-=1
        #             if sCount[s[l]] == tCount[s[l]]:
        #                 matches+=1
        #             elif sCount[s[r]]-1 == tCount[s[r]]:
        #                 matches-=1
        #             l+=1
        #         res = s[l:r] if len(s[l:r])<len(res) else res
        #     print("R: " + str(r))
        #     print(matches)
        #     sCount[s[r]] += 1
        #     print(s[r])
            
        #     if sCount[s[r]] == tCount[s[r]]:
        #         matches+=1
        #     elif sCount[s[r]]-1 == tCount[s[r]]:
        #         matches-=1
            

        # return res            

        
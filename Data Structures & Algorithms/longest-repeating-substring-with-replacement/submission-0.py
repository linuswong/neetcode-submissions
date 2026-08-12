class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 1
        replacements = k 
        count = {}
        maxf=0


        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxf = max(maxf,count[s[r]])

            while r-l - maxf >= k:
                count[s[l]]-=1
                l+=1
            longest = max(longest,r-l+1)


            # if (r-l) - count[s[l]] >= k:
            #     print(r-l)
            #     longest = r-l + 1 if r-l + 1 > longest else longest
            # else:
            #     print(count)
            #     count[s[l]] -= 1
            #     l+=1
            

        return longest
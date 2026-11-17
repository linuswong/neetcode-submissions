class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start = 1
        # i = 0
        # digits = digits[::-1]

        # while start:
        #     if i < len(digits):
        #         if digits[i] == 9:
        #             digits[i] = 0
        #         else:
        #             digits[i]+=1
        #             start = 0
        #     else:
        #         digits.append(start)
        #         start = 0
        #     i += 1

        
        # return digits[::-1]

        tot = 0
        for i in range(len(digits)):
            tot += digits[i] * 10**(len(digits)-1-i)
        
        tot+=1
        print(tot)

        res = []
        while(tot>0):
            res.append(tot%10)
            tot//=10
        res.reverse()
        return res

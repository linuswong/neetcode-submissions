class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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

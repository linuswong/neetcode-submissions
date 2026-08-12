class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for i in s1:
            count[i] = count.get(i,0)+1
        # print(count)
        
        res = True
        for i in range(0,len(s2)-len(s1)+1,1):  
            # print(i)
            tempcount = count.copy()
            res = True
            for j in range(len(s1)):
                if s2[j+i] in tempcount:
                    tempcount[s2[j+i]] -= 1
                    # print(tempcount)
                    # print("Count:",end=" ")
                    # print(count)
                else:
                    res = False
                    break
            if res and all(value == 0 for value in tempcount.values()):
                return True

        return False


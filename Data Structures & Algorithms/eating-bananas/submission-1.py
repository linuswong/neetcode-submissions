class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)
        min_k = max(piles)

        while l <= r:
            k = (l + r)//2
            count = 0
            for b in piles:
                count += math.ceil(b/k)
                if count > h:
                    break
            
            if count <= h:
                min_k = min(k,min_k)
                r = k-1
            else:
                l = k+1

        return min_k

        # if len(piles) == 1:
        #     return piles[0]
    
        # sp = sorted(piles)
        # sp = sp[::-1]
        # k =  sp[0]

        # for i in range(len(sp)):
        #     count = 0
        #     for j in range(len(sp)):
        #         count += -(-sp[j] // -k)
        #         if count > h:
        #             break
        #     if count <= h:
        #         k = sp[i]

        # return k
    

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l,r = 0, len(height)-1

        maxL= height[l] 
        maxR = height[r]

        tot = 0
        cont = True
        while cont:
            
            if r==l:
                cont = False
            calc = 0
            if maxL <= maxR:
                calc = maxL - height[l]
                tot += calc if calc > 0 else 0
                maxL = height[l] if height[l] > maxL else maxL    
                l+=1
            else:
                calc = maxR - height[r]
                tot += calc if calc > 0 else 0
                maxR = height[r] if height[r] > maxR else maxR
                r-=1
            
        return tot
                






        # if len(height) < 3:
        #     return 0

        # maxLeft = [0] * len(height)
        # maxRight = [0] * len(height)

        # maxLeft[0] = 0
        # maxRight[len(height)-1] = 0

        # for i in range(1,len(height)-1):
        #     if height[i-1] > maxLeft[i-1]:
        #         maxLeft[i] = height[i-1]
        #     else:
        #         maxLeft[i] = maxLeft[i-1]
        #     if height[-i] > maxRight[-i]:
        #         maxRight[-i-1] = height[-i] 
        #     else:
        #         maxRight[-i-1] = maxRight[-i]

        # tot = 0
        # for i in range(len(height)):
        #     calc = min(maxLeft[i],maxRight[i])- height[i]
        #     tot += calc if calc > 0 else 0
        # return tot

            



        # l,r = 0, len(height)-1
        # area = sum(height)

        # # while l != r:


            

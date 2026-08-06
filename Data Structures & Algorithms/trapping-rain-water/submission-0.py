class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0] = 0
        maxRight[len(height)-1] = 0

        for i in range(1,len(height)-1):
            if height[i-1] > maxLeft[i-1]:
                maxLeft[i] = height[i-1]
            else:
                maxLeft[i] = maxLeft[i-1]
            if height[-i] > maxRight[-i]:
                maxRight[-i-1] = height[-i] 
            else:
                maxRight[-i-1] = maxRight[-i]

        tot = 0
        for i in range(len(height)):
            calc = min(maxLeft[i],maxRight[i])- height[i]
            tot += calc if calc > 0 else 0
        return tot

            



        # l,r = 0, len(height)-1
        # area = sum(height)

        # # while l != r:


            

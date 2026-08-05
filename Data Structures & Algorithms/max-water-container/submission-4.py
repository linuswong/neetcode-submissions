class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        area = min(heights[l],heights[r])*(r-l)

        while l != r:
            val =min(heights[l],heights[r])*(r-l)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            area = val if val > area else area

        return area






        # l,r = 0,len(heights)-1
        # area = min(heights[l],heights[r])*(r-l)

        # while l != r:
        #     val = 0
        #     l_inc = min(heights[l+1],heights[r])*(r-(l+1))
        #     r_dec = min(heights[l],heights[r-1])*(r-1-l)
        #     if  l_inc > r_dec:
        #         l+=1
        #         val = min(heights[l],heights[r])*(r-(l))
        #     elif r_dec > l_inc:
        #         r-=1
        #         val = min(heights[l],heights[r])*((r)-l)
        #     else:
        #         if heights[r-1]>heights[l+1]:
        #             r-=1
        #         else:
        #             l+=1
            
        #     area = val if val > area else area
        # return area


        # l,r = 0, 1
        # area = min(heights[l],heights[r])*(r-l)
        # while l != r and r<len(heights)-1:
        #     val = 0
        #     l_inc = min(heights[l+1],heights[r])*(r-(l+1))
        #     r_inc = min(heights[l],heights[r+1])*((r+1)-(l))

        #     val = 0
        #     if l_inc > r_inc:
        #         l+=1
        #         val = l_inc
        #     elif r_inc > l_inc:
        #         r+=1
        #         val = r_inc
        #     else:
        #         if heights[r+1]>heights[l+1]:
        #             r+=1
        #         else:
        #             l+=1
        #     area = val if val > area else area
        # return area

        
            


            






        # l,r =(0,0),(0,0)
        # res = min(l[1],r[1])*(l[0]-r[0])

        # for i in range(len(heights)-1):
        #     l = (i,heights[i])
        #     for j in range(i+1, len(heights)):
        #         r= (j,heights[j])
        #         res = min(l[1],r[1])*(r[0]-l[0]) if min(l[1],r[1])*(r[0]-l[0]) > res else res
        # return res


        
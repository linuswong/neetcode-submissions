class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 if len(nums1) <= len(nums2) else nums2
        b = nums1 if len(nums1) > len(nums2) else nums2

        tot = len(a) + len(b)
        half =  tot//2

        l,r =  0, len(a)-1
        while True:
            i = (l+r) //2 # A
            j = half - i - 2 # B

            aLeft = a[i] if i >= 0 else float("-infinity")
            aRight = a[i+1] if (i +1) < len(a) else float("infinity")

            bLeft = b[j] if j >= 0 else float("-infinity")
            bRight = b[j+1] if (j+1) < len(b) else float("infinity")

            if aLeft <= bRight and bLeft <=aRight:
                if tot % 2:
                    return min(aRight, bRight)
                
                return (max(aLeft,bLeft) + min(aRight,bRight)) /2
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1





        
        # tot = len(nums1) + len(nums2)
        # half = tot // 2
        # l, r = 0, len(nums1) + len(nums2)-1

        # a = len(nums1)
        # b= len(nums2)

        # while l < r:
            
        #     ah = a // 2
        #     bh = b //2










        # #BRUTE FORCE O(N LOG N)
        # comb = nums1 + nums2
        # comb = sorted(comb)
        # l, r = len(comb)//2 - 1, len(comb) // 2

        # return (comb[l] + comb[r])/2 if len(comb)%2 == 0 else comb[r]
            


        

        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l, r = 0, len(nums1) + len(nums2)-1

        # while l < r:
            






        # #BRUTE FORCE O(N LOG N)
        comb = nums1 + nums2
        comb = sorted(comb)
        print(comb)
        l, r = len(comb)//2 - 1, len(comb) // 2

        return (comb[l] + comb[r])/2 if len(comb)%2 == 0 else comb[r]
            


        

        
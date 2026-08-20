class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1
        m = l + (r-l)//2
        while l <= r:
            if nums[l] < nums[r]:
                return min(res,nums[l])
            m = l + (r-l)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r= m -1
        return res
        # l = 0 = 3
        # r = 5 = 2

        # idx = 0  + 5//2 = 2 = 5
        # before = 1 = 4
        # after = 3 = 6

        # l = 0 = 3
        # r = 4%6 = 4 = 1


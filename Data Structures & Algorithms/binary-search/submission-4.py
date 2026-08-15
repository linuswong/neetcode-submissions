class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)

        while l<r:
            idx = l+(r-l)//2
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                l=idx +1
            else:
                r=idx
            if idx == 0:
                return -1
        return -1
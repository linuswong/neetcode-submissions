class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        res= []
        q = deque()
        l,r =0,0

        while r < len(nums):
            
            while q and nums[r]> nums[q[-1]]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if r+1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
            
        return res

        # if len(nums) == 1:
        #     return [nums[0]]

        # res = []
        # my_deque = deque()
        # l=0

        # for i in range(k-1):
        #     while my_deque and nums[i]>my_deque[-1]:
        #         my_deque.pop()
        #     my_deque.append(nums[i]) 

        # for r in range(1,len(nums)):
        #     while my_deque and nums[r]>my_deque[-1]:
        #         my_deque.pop()
        #     my_deque.append(nums[r])


            #if nums[r]>my_deque[-1]:
                




        # if len(nums) == 1:
        #     return [nums[0]]

        # res = []
        # l=0
        # curMax,curMaxIdx= nums[0], 0

        # for i in range(k-1):
        #     if nums[i] > curMax:
        #         curMax = nums[i]
        #         curMaxIdx = i

        
        # for r in range(k-1,len(nums)):
        #     if nums[r] > curMax:
        #         curMax = nums[r]
        #         curMaxIdx = r
        #     if l == curMaxIdx:
        #         temp = nums[l+1:r+1]
        #         print(temp)
        #         curMax = max(temp)
        #         curMaxIdx = temp.index(curMax)

        #     l+=1

        # return res




        # if len(nums) == 1:
        #     return [nums[0]]

        # res = []
        # l=0
        # cur,curidx= nums[0], 0
        # for r in range(k-1,len(nums)):
        #     temp = (nums[l:r+1])
        #     temp.sort()
        #     res.append(temp[len(temp)-1])
        #     l+=1

        # return res

        
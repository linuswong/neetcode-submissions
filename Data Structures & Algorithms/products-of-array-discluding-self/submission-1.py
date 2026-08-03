class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            output.append(1)
            for j in range(len(nums)):
                if i!=j:
                    output[i]*=nums[j]

        return output
                




        # output = []
        # tot = 1
        # zero = False
        # for i in nums:
        #     if i != 0:
        #         tot *= i
        #     else:
        #         zero = True
        
        # for i in nums:
        #     if i == 0:
        #         output.append(tot)
        #     elif zero:
        #         output.append(0)
        #     else:
        #         output.append(int(tot/i))


        # return output
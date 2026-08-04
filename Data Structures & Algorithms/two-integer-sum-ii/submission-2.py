class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r =0,len(numbers)-1

        while l != r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]


        # for i in range(len(numbers)):
        #     nn = target - numbers[i]
        #     for j in range(i+1,len(numbers),1):
        #         if numbers[j] == nn:
        #             return [i+1,j+1]



        # for i in range(len(numbers)):
        #     needed_n = target - numbers[i]
        #     for j in range(len(numbers),i,1):
        #         if i==j:
        #             pass
        #         if needed_n == numbers[j]:
        #             return [i,j]


        
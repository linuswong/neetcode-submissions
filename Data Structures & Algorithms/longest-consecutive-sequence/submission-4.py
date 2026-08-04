class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max = 0

        for n in nums:
            if n-1 not in my_set:
                length = 0
                while(n+length) in my_set:
                    length +=1
                    max = length if length>max else max


        return max

                


        # for i in range(len(my_set)):
        #     if not my_set.contains(my_set[i] - 1):
        #         starters.append(my_set[i])
        # for i in range(len(my_set)):
        #     if my_set.contains(my_set[i]+1):
        #         counter += 1
        #         max = counter if counter > max else max
        #     else:
        #         continue





        # my_dict = {}
        # if(len(nums) == 0):
        #     return 0
        # for i in range(len(nums)):
        #     my_dict[nums[i]] = 1
        # print(my_dict)
        
        # start = min(my_dict) # O(n)
        # counter = 1
        # max = counter
        # for i in range(len(nums)):
        #     if my_dict.get(start + 1) != None:
        #         start +=1
        #         counter +=1
        #         max = counter if counter > max else max
        #     else:
        #         next_candidates = [k for k in my_dict if k > start]
                
        #         if next_candidates:
        #             start = min(next_candidates)  # Jump to the next lowest available number
        #             counter = 1
        #             max = counter if counter > max else max
        #         else:
        #             break
        # return max


        # my_dict = {}
        # for i in range(len(nums)):
        #     my_dict[i] = 1
        #     for j in range(len(my_dict)):
        #         if nums[i] == my_dict[j] + j:
        #             my_dict[j] += 1
        # return max(my_dict.values())

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numhash = { }
        freq = [[] for i in range(len(nums)+1)]

        for i in nums: 
            numhash[i] = 1 + numhash.get(i,0)
        for key, v in numhash.items():
            freq[v].append(key)
        print(freq)
        result = []
        
        for i in range(len(freq) -1, 0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
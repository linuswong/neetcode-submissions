class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numhash = { }

        for i in nums:
            if i not in numhash:
                numhash[i] = 0
            numhash[i] += 1

        final = []
        for i in range(k):
            maxval = max(numhash, key=numhash.get)
            final.append(maxval)
            numhash.pop(maxval)
        return final
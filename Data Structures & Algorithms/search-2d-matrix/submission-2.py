class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mod = len(matrix[0])

        l,r=  0, len(matrix) * mod
        
        while l<r:
            idx = l + (r-l)//2
            if matrix[idx//mod][idx % mod] == target:
                return True
            elif idx == l:
                break
            elif matrix[idx//mod][(idx % mod)] > target:
                r = idx
            elif matrix[idx//mod][idx % mod] < target:
                l = idx
            
        return False

        # r=6 = 16
        # l=0

        # l=3 = 7
        # r= 6

        # l= 4 = 10
        # r = 6

        # l=5 = 11
        # r=  6



        
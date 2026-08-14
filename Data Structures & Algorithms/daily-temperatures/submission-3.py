class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res =[0] * len(temperatures)

        s = []
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]]<temperatures[i]:
                res[s[-1]] = i-s[-1]
                s.pop()

            s.append(i)
        return res




        # res = [0] * len(temperatures)
        # res[len(temperatures)-1]  = 0

        # q = deque()
        # s = []
        # #q.append(temperatures[len(temperatures)-1])

        # for i in range(len(temperatures)-1,0,-1):
        #     print(temperatures[i])
        #     count = 0 
        #     while q and temperatures[i] < q[-1]:
        #         count +=1
        #         s.append(q.pop())
        #     q.append(temperatures[i])
        #     while s:
        #         q.append(s.pop())
            
        #     print(q)
        #     res[i] = count 

        # return res

        
        
        # res =[0] * len(temperatures)

        # for i in range(len(temperatures)-1):
        #     count =0
        #     for j in range(i+1,len(temperatures)):
        #         count+=1
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = count
        #             break
                    
        
        # return res

        
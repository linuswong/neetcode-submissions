class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p,s in zip(position,speed)]

        c= []
        for p,s in sorted(pair)[::-1]:
            ttt = (target - p)/ s
            if not c:
                c.append(ttt)
            elif ttt > c[-1]:
                c.append(ttt)

        return len(c)

            

        # c = []

        # for i in range(len(position)-1):
        #     for j in range(i+1,len(position)):
        #         if speed[i] == speed[j]:
        #             if position[i] == position[j]:
        #                 c.append(0,speed[i])
        #             break
        #         time_meet = (position[i] -position[j]) / (speed[j] - speed[i])
        #         pos_meet = (time_meet)* speed[i] + position[i]

        #         if pos_meet <= target and pos_meet>0:
        #             fleet_speed = speed[i] if speed[i] < speed[j] else speed[j]
        #             c.append((pos_meet, fleet_speed))
        #         print(c)
        #         else:
        #             c.append()

        # return len(c)



        # a -> speed: 3
        # -> pos: 1
        # b -> speed :2
        # -> pos:4

        # target:20

        # a_pos

        # a_pos + a_sp * x = b_pos + b_sp * x

        # a_pos - b_pos = x*(b_sp - a_sp)
        # x = (a_pos-b_pos)/(b_sp-a_sp)   
        # 0,2
        # 4,1
        # 0-4 / 1-2
        # -4/-1 = 4

        # 0,2,4,6,8,10
        # 4,5,6,7,8

        # 4,1
        # 0,2
        # 4
        # 4,5,6,7,8
        # 0,2,4,6,8

        # 1,3
        # 4,2

        # -3/-1 = 3

        # 1,4,7,10
        # 4,6,8,10


        # (a_pos+x) + (a_sp*t) = (b_pos+x) + (b_sp*t)
        # a_pos


        
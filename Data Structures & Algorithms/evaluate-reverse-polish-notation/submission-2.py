class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t == '+' or t =='-' or t =='*' or t =='/':
                r = s.pop()
                l=s.pop()
                #print(str(l)+t+str(r))
                if t =='+':
                    s.append(l + r)
                elif t =='-':
                    s.append(l - r)
                elif t =='*':
                    s.append(l * r)
                else:
                    if (l/r < 0):
                        s.append(-(l // -r)  )
                    else:
                        s.append(l // r)
            else:
                s.append(int(t))

        return s.pop()
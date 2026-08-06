class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        
        for i in s:
            if i =="(" or i == "[" or i =="{":
                stack.append(i)
            else:
                brace=""
                if stack:
                    brace = stack.pop()
                    print(brace)
                if (brace == "(" and i == ")") or (brace == "[" and i == "]") or (brace == "{" and i == "}"):
                    continue
                else:
                    return False
        return not stack


            # if i == "(":
            #     s_par.append(i)
            # elif i == "[":
            #     s_sq.append(i)
            # elif i =="{":
            #     s_cur.append(i)

            # else:
            #     if i == ")" and s_par:
            #         s_par.pop()
            #     elif i == "]" and s_sq:
            #         s_sq.pop()
            #     elif i =="}" and s_cur:
            #         s_cur.pop()
            #     else:
            #         return False
        
        return  not (s_par and s_sq and s_cur)

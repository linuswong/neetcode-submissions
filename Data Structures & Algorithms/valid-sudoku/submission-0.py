class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numsIn3by3 = [[[] for i in range(3)] for j in range(3)]
        for i in range(len(board)):
            curRow=[0]*10
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                else:
                    if curRow[int(board[i][j])] == 0:
                        curRow[int(board[i][j])] = 1
                    else:
                        return False
                    numsIn3by3[int(i/3)][int(j/3)].append(int(board[i][j]))

        for i in range(len(board)):
            curCol=[0]*10
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                else:
                    if curCol[int(board[j][i])] == 0:
                        curCol[int(board[j][i])] = 1
                    else:
                        return False

        for row in numsIn3by3:
            for box in row:
                if len(box) != len(set(box)):
                    return False

        return True

    
    # 0
    # [][][]
    # [][][]
    # [][][]
    #      8


        
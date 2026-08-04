class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if(board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        return True




        # numsIn3by3 = [[[] for i in range(3)] for j in range(3)]
        # for i in range(len(board)):
        #     curRow=[0]*10
        #     for j in range(len(board[i])):
        #         if board[i][j] == ".":
        #             continue
        #         else:
        #             if curRow[int(board[i][j])] == 0:
        #                 curRow[int(board[i][j])] = 1
        #             else:
        #                 return False
        #             numsIn3by3[int(i/3)][int(j/3)].append(int(board[i][j]))

        # for i in range(len(board)):
        #     curCol=[0]*10
        #     for j in range(len(board[i])):
        #         if board[j][i] == ".":
        #             continue
        #         else:
        #             if curCol[int(board[j][i])] == 0:
        #                 curCol[int(board[j][i])] = 1
        #             else:
        #                 return False

        # for row in numsIn3by3:
        #     for box in row:
        #         if len(box) != len(set(box)):
        #             return False

        # return True

    
    # 0
    # [][][]
    # [][][]
    # [][][]
    #      8


        
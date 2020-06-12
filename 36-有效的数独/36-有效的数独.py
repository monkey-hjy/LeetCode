# @Time : 2020/6/12 15:43 
# @Author : Monkey
# @Software: PyCharm

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判断行列符不符合要求
        for i in range(len(board)):
            row = []
            column = []
            for j in range(len(board[i])):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row.append(board[i][j])
                if board[j][i] != '.' and board[j][i] in column:
                    return False
                column.append(board[j][i])
        # 判断九宫格是否符合要求
        # 四个for循环有点傻。。。目前只想到这一种依次遍历九宫格的方法
        for row in range(3):
            for column in range(3):
                lst = []
                for i in range(row*3, (row+1)*3):
                    for j in range(column*3, (column+1)*3):
                        if board[i][j] != '.' and board[i][j] in lst:
                            return False
                        lst.append(board[i][j])
        return True



# More Veeva Technical Prep 
# https://leetcode.com/problems/valid-sudoku/

from typing import List 
class Solution:
    def isValidSudoku(board: List[list[str]]) -> bool:
        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9): 
                value = board[r][c]
                if value == ".":
                    continue
                
                box = (((r // 3) * 3 ) + c // 3)

                if value in row_list[r]:
                    return False
                if value in col_list[c]:
                    return False
                if value in box_list[box]:
                    return False

                row_list[r].add(value) 
                col_list[c].add(value)
                box_list[box].add(value)
        return True



        

        
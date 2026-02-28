#Veeva Prep 

from typing import List 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        collected = []
        def backtrack(path, openCount, closeCount):

            if len(path) == (2 * n): 
                collected.append(path)
                return 

            if openCount < n: 
                backtrack(path + "(", openCount + 1, closeCount)

            if closeCount < openCount: 
                backtrack(path + ")", openCount, closeCount + 1)

        
            
        backtrack("", 0, 0)
        return collected   



            
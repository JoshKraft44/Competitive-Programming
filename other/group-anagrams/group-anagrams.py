# more veeva prep 
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) 
        for str in strs: 
            key = tuple(sorted(str))
            dict[key].append(str) 

        return list(dict.values())

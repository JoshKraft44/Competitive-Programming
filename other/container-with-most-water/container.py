# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            maxWater = max(maxWater, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater


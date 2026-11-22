class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Use two pointer
        - left = 0
        - right = len(heights) - 1

        Get the height
        - this value gives height at which water won't spill out.
        - min(heights[left], heights[right])

        Get the width
        - right - left

        Find the area
        - minimum height * width

        Case 1: if heights[left] <= heights[right] -> left += 1
        Case 2: if heights[left] > heights[right] -> right -= 1

        Return the area
        """

        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            area = height * width
            res = max(res, area)

            if heights[left] <= heights[right]:
                left += 1
            
            else:
                right -= 1

        return res


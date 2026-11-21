class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Convert the nums list to a set.
        Intialize longest_streak = 0 (final result)
        Iterate through the set. For each element
        - check if num - 1 is in the list.
            - If no, that is the start of a streak.
            - Increment the current_streak (current_streak = 1)
            - Check if num + current_streak exist in the set.
                - If yes, increment the current_streak.
            - Compare the longest_streak and current_streak. Save the higher value.
        - Return the longest_streak.
        """

        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_streak = 1
                while (num + current_streak) in nums_set:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

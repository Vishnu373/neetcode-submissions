class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        List is empty, return 0.
        Else, sort the list.

        Iterate through the list,
        - start at index 1 and ending will be len(nums) - 1.
        - Check for duplicates
            - see if the current element is same as the previous one.
            - if yes, skip it
        - If the current element is same as the previous element + 1.
            - Increment the streak
        - If the current element isn't same as the previous element + 1.
            - Reset the streak
        - Compare the streaks so far.
        Return the latest value of streak variable.
        """

        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                current_streak += 1
            
            else:
                current_streak = 1
            
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak


            



        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use hashset to store unique characters.
        Use sliding window to get the longest substring.

        Intialize am empty hashset.
        Set left = 0, right = 0

        Iterate through the string using right,
        - check if the character is in the set,
            - if yes, remove that character
               - set left = left + 1, 
            - if no, add it
                - store the window length or set length

        return the window length
        """

        char_set = set()
        longest_window = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            longest_window = max(longest_window, right - left + 1)
        
        return longest_window



        
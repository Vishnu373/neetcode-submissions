class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        - Hashset -> storing unique elements
        - Applying sliding window

        Set left pointer (window beginning) as 0.
        Iterate through the string.
        - check if the current element is in set.
            - if yes,
                - remove the left most / first element from the set (as it's a duplicate)
                - increment left pointer (updating set beginning)
            - if no,
                - add the element
                - calculate the window length which is iterating variable - current index pointer of set + 1

        - return the window length 
        """

        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            res = max(res, (right - left + 1))
        
        return res


        
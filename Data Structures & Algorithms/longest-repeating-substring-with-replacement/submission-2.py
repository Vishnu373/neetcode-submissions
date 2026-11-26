class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - Sliding window + hashmap
        - Hashmap to store frequency of individual characters.
            {key - character, value - frequency of that character}

        - left, right = 0, 0
        - most_freq = {}
        - longest_window = 0
        
        - Iterate through the string (window)
            - Fill up the hashmap
            - Check if window is valid or not
                - if yes (Condition - current_window_length - most_freq[char] <= k)
                    - longest_window = max(current_window_length, longest_window)
                    - right += 1
                - else (invalid window)
                    - shrink the window (left += 1)
                    - most_freq[char] - 1 
        """

        freq = {}
        longest = 0
        left = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest








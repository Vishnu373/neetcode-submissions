class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        0. Length of the two strings are same -> proceed. Else return False.
        1. Create 2 empty hashmaps - one string each.
        2. For each string, store the each character and it's frequency as key-value.
        3. Compare the two hashmaps based on the key.
        4. If the key and it's value match. Return True, it's an anagram. Else, return False - not an anagram. 
        """

        # base condition
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        # Iterate through the strings
        for i in range(len(s)):
            # build the hashmaps
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # comparing the hashmaps
        for ch in s:
            if count_s[ch] != count_t.get(ch, 0):
                return False

        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Create a alphaNum(ch) which takes single character as an argument.
        - Purpose:- check whether the character is a alphabet or number.
        - Checks whether ASCII of given character falls under the uppercase alphabet (A-Z), lowercase alphabet(a-z) or numbers (0 - 9) ASCII range.

        Utilize two pointer approach.
        - left intialized as 0 (first index)
        - right intialized as len(s) - 1 (last index)

        Iterate through the string until left < right.
        - Keep moving forward until it's alphanumeric character.
        - Keep moving backward until it's alphanumeric character.

        - Compare the lowercase of left and right indexed element.
            - if they don't match return false (not a palindrome)
            - if they match,
                - increase left pointer
                - decrease right pointer

        - If the loop finishes without any mismatch, return true. 
        """

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

    def alphaNum(self, ch):
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))
class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        For each element, we need
        - length of the string
        - an indication when the next element is starting
        """

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        Iterate through the string until it's the end.
        - Pointer j be set to i. 
        - Keep incrementing j until it's not "#".
            - if it's "#"
            - The intermediate left element is the length.
        - The intermediate right of # to the length is a word, add it to result.
        - Final return the res list.
        """

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


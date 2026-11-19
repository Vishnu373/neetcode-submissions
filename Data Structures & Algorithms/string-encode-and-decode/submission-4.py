class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1: length + j + 1]
            res.append(word)

            i = length + j + 1
        
        return res


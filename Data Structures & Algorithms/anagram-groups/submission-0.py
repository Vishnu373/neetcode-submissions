class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)

        return hashMap.values()
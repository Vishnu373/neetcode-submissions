class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create an empty hashmap
        - key = frequency of characters per unique elements
        - value = elements that match the frequency, i.e., original string

        Iterate through the list, for each element,
        - Create an empty list with all zeros length - 26.
        - For each character in the element
            - get the frequency and increment the count of that corresponding index.
            - use ord(character)
        - Convert the list into a tuple and use it as key.
        - Append the strings which match that frequency as values.
        - Return hashmap values as a list
        """

        grouped = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            grouped[tuple(count)].append(s)
        
        return list(grouped.values())
              
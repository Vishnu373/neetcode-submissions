class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Hashmap:-
        key - frequency of character
        value - list of original strings

        Iterate through the list, for each element,
        - create a 26 sized list with zeros in it.
        - increment the count of correpsonding index.
            Meaning:- act => [1, 0, 1, 0, 0, .... 1, ...., 0]
            - Convert the this list into a tuple and use it as the key.
        - Add the string to the associated list/key.
        """

        grouped = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            grouped[tuple(count)].append(s)
        
        return list(grouped.values())
              
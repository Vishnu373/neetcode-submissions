class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Build Freq map - it's a list of list.
        - where each index indicates the frequency of the element
        - Maximum length is equal to length of original list i.e., a number can only appear as many times as the length of the original list.

        In order to build this, first create an hashmap with each element and it's frequency as key-value pair.

        Then, iterate through the freq list in reverse. Repeat the iteration until it's equal to k.
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


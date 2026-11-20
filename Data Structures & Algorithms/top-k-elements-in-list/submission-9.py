class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create a hashmap with element and it's frequency.
        Create a freq list (list of list). It's length is equal to the list of original list.
        Store each element from the hashmap into freq list such that the index is the value (element's frequency) and key is the element.

        Iterate through the freq list in reverse.
        - Append the elements to res list only until the length of res equals to k.
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) == k:
                    return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # Get count of each element in hasMap
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Add the count to freq
        # freq -> index - count, value - element
        for n, c in count.items():
            freq[c].append(n)

        # Get k most frequent elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



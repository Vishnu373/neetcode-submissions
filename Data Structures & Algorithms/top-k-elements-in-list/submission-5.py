class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sorted_count = sorted(count.items(), key = lambda freq: freq[1], reverse = True)
        res = [item[0] for item in sorted_count[:k]]
        
        return res


        

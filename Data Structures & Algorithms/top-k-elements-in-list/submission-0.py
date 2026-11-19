class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for ele in nums:
            if ele not in hashMap:
                hashMap[ele] = 1
            hashMap[ele] += 1

        sorted_hashMap = sorted(hashMap.items(), key = lambda item: item[1], reverse = True)
        frequent_elements = [ele[0] for ele in sorted_hashMap[:k]]

        return frequent_elements

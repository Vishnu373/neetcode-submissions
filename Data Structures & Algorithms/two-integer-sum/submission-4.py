class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        0. Create an empty hashmap, which will store the element as key and index as it's value.
        1. Iterate through the array.
        2. For each element, find the difference with the target.
        3. Search for the difference in the hashmap.
        4. If difference not present, add the element to hashmap.
        5. When you get the difference, return the current element index and difference element index.
        """

        pairs = {}
        for i, num in enumerate(nums):
            difference = target - num

            if difference in pairs:
                return [pairs[difference], i]
            
            pairs[num] = i
        
        return []

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1. Create an empty set.
        2. Insert each element into set.
        3. As you insert, if the element is already present return True
        else return False.
        """

        unique = set()

        for num in nums:
            if num not in unique:
                unique.add(num)
            
            else:
                return True

        return False
        
        
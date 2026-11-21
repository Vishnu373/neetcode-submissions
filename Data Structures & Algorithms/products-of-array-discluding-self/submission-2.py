class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Iterate through the list
        - calculate the prefix
        - then calculate postfix

        prefix
        - Intially set to 1.
        - for each element in the list,
         - multiply prefix with each element, update prefix with result.
         - the res becomes the output element.

        postfix
        - Intially set to 1
        - for each element in the output list (reverse order)
            - res[i] = postfix * res[i]
            - Update the postfix by postfix * nums[i]

        In the end return the resultant list.
        """

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
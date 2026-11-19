class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 1. target is at mid
            if target == nums[mid]:
                return mid

            """
            Case 2:-
            the mid element is in left sorted array
            - target is greater than mid, search in right
            - target is less than mid and target is less than left most element, search in right
            - target is less than mid and target is greater than left most element, search in left
            """
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

                else:
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                
                else:
                    left = mid + 1

        return -1

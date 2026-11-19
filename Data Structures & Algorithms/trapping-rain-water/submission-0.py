class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        n = len(height)

        max_left = [0] * n
        max_right = [0] * n
        min_arr = [0] * n


        # maximum left array
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        # maximum right array
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        # minimum between max left and right
        for i in range(n):
            min_arr[i] = min(max_left[i], max_right[i])

            # Trapped water
            trapped = min_arr[i] - height[i]

            if trapped > 0:
                water_trapped += trapped

        return water_trapped
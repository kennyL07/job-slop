class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = [0 for i in range(len(height))]
        suffixMax = [0 for i in range(len(height))]

        prefix = 0
        suffix = 0
        for i in range(len(height)):
            if height[i] > prefix:
                prefixMax[i] = height[i]
                prefix = height[i]
            else:
                prefixMax[i] = prefix
            if height[len(height) - i - 1] > suffix:
                suffixMax[len(height) - i - 1] = height[len(height) - i - 1]
                suffix = height[len(height) - i - 1]
            else: 
                suffixMax[len(height) - i - 1] = suffix
        volTotal = 0
        for i in range(len(height)):
            volTotal += min(prefixMax[i], suffixMax[i]) - height[i]
        return volTotal
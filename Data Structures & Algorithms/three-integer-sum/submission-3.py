class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] > nums[i] * -1:
                    k -= 1
                elif nums[j] + nums[k] < nums[i] * -1:
                    j += 1
                elif nums[j] + nums[k] == nums[i] * -1:
                    if not ([nums[i], nums[j], nums[k]] in solutions):
                        solutions.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1

        return solutions
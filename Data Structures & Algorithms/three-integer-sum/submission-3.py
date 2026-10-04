class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k = 0

        while k < len(nums):
            i = k + 1
            j = len(nums) - 1
            target = -nums[k]
            # for nums[k] duplicate

            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    # for num[i] duplicate
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    # for num[j] duplicate
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
            k += 1
            while k < len(nums) and nums[k] == nums[k-1]:
                k += 1
        return res



                
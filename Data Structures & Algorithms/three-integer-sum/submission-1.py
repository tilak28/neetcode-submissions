class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for k in range(len(nums)):
            # for nums[k] duplicate 
            if k > 0 and nums[k] == nums[k-1]:
                continue

            i = k + 1
            j = len(nums) - 1

            while i < j:

                target = -nums[k]
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
        return res



                
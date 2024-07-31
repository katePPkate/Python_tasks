class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                if min == nums[i-1]:
                    result.append(str(min))
                else:
                    result.append(str(min) + "->" + str(nums[i-1]))
                min = nums[i]
        if min == nums[-1]:
            result.append(str(min))
        else:
            result.append(str(min) + "->" + str(nums[-1]))
        return result


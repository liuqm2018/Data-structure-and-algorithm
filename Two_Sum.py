class Solution(object):
    def Two_Sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
a = Solution()
print(a.Two_Sum([2,7,11,15],9))

#Two_Sum([2,7,11,15],9)

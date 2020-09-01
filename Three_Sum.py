class Solution():
    def Three_Sum(self,nums):
        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0 :
                return res
            if (i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while L<R:
                if (nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]== nums[L+1]):
                        L = L+1
                    while (L<R and nums[R]== nums[R-1]):
                        R = R -1
                    L = L+1
                    R = R-1
                elif (nums[i]+nums[L]+nums[R]<0):
                    L = L+1
                else:
                    R = R-1
        return res
a = Solution()
print(a.Three_Sum([-1,0,1,2,-1,-4]))
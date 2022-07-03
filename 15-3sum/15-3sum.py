class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        res = set()
        l = len(nums)
        for i in range(l-2):
            if nums[i] > 0:
                break
            j = i + 1
            k = l - 1
            while j<k:
                if nums[j] + nums[k] == -nums[i]:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
                    
        return res
        
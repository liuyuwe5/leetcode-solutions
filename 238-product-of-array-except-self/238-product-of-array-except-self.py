class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if 0 in nums:
            index0 = nums.index(0)
            product0 = 1
            for i in range(len(nums)):
                if i != index0:
                    product0 *= nums[i]
            return [0] * index0 + [product0] + [0] * (len(nums) - index0 - 1)
        else:
            res = []
            product = 1
            for i in nums:
                product *= i
            for i in nums:
                res.append(product/i)
            return res
                
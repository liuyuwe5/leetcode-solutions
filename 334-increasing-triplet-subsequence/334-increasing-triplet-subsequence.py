class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
      
        if len(set(nums)) < 3:
            return False
        
        for i in range(len(nums) - 2):
            j = i + 1
            while j < len(nums) - 1:
                if nums[i] >= nums[j]:
                    j += 1
                else: 
                    k = j + 1
                    while k < len(nums):
                        if nums[i] < nums[j] and nums[j] < nums[k]:
                            return True
                        k += 1
                    j += 1
            
        return False
            
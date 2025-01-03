class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        sum_all = sum(nums)
        sum_left = 0
    
        for i in range(len(nums)-1):
            sum_left = sum_left+nums[i]
            sum_right = sum_all-sum_left
            if sum_left >= sum_right:
                count +=1

        return count

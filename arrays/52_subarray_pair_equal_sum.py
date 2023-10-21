# Link: https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        freq = {}
        for i in range(len(nums)-1):
            key = nums[i] + nums[i+1]
            if key in freq:
                return True
            else:
                freq[key] = True
        return False

"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

Solution:

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[i for i in range(1,len(nums)+1)]
        a1=set(nums)
        a2=set(l)
        ans=sorted(a2-a1)
        return ans

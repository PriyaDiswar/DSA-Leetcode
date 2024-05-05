"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def count(goal):
            l,r=0,0
            sm=0
            c=0
            if goal<0:
                return 0
            while r<=len(nums)-1:
                sm+=nums[r]
                while sm>goal:
                    sm-=nums[l]
                    l+=1
                c+=(r-l+1)
                r+=1
            return c
        return count(goal)-count(goal-1)
            

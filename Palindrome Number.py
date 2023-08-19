"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

Solution:

class Solution(object):
    def isPalindrome(self, x):
        b=x
        s=0
        while x>0:
            s=s*10+(x%10)
            x=x//10
        if s==b:
            return (True)
        else:
            return (False)

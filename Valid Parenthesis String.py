"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maxi,mini=0,0
        for i in s:
            if i=="(":
                maxi,mini=maxi+1,mini+1
            elif i==")":
                maxi,mini=maxi-1,mini-1
            else:
                maxi,mini=maxi+1,mini-1
            if maxi<0:
                return False
            mini=max(mini,0)
        return mini==0
            

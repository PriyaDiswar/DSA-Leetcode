"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 """
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=0
        temp=list(s)
        for i in range(len(s)):
            if temp[i]=="(":
                counter+=1
            elif temp[i]==")":
                if counter==0:
                    temp[i]="#"
                else:
                    counter-=1
        
        for i in range(len(s)-1,-1,-1):
            if counter>0 and temp[i]=="(":
                temp[i]="#"
                counter-=1
        res=''.join(k for k in temp if k!="#")
        return res

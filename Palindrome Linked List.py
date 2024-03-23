"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        count=1
        while temp.next:
            count+=1
            temp=temp.next
        temp=head
        lis=[]
        for i in range(count//2):
            lis.append(temp.val)
            temp=temp.next
        if count%2:
            temp=temp.next
        i=-1
        while temp:
            if temp.val!=lis[i]:
                return False
            i-=1
            temp=temp.next
        return True

"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are remove
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        temp=prev
        head=None
        mx=float("-inf")
        while temp:
            if temp.val>=mx:
                mx=temp.val

                nxt=temp.next
                temp.next=head
                head=temp
                temp=nxt
            else:
                temp=temp.next
        return head
        

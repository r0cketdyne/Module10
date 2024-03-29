# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        current = dummy
        
        # Merge the lists while both are non-empty
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Append the remaining nodes from the non-empty list
        current.next = l1 if l1 else l2
        
        # Return the head of the merged list (next node after the dummy node)
        return dummy.next












#my prototype. coded from scratch.
#actually works
"""
list1 = [1,2,4]
list2 = [1,3,4]

def mergeTwoLists(list1, list2):
        
       morph1 =  sorted(list1)
       morph2 = sorted(list2)
       
       morph_final = sorted(morph1 + morph2) 
       print(morph_final)
     
mergeTwoLists(list1, list2)

###You are given the heads of two sorted linked lists list1 and list2.
###Merge the two lists into one sorted list. 
###The list should be made by splicing together the nodes of the first two lists.
###Return the head of the merged linked list.


#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Example 2:

#Input: list1 = [], list2 = []
#Output: []
#Example 3:

#Input: list1 = [], list2 = [0]
#Output: [0]
"""
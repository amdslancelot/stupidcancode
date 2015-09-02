# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.val == val:
            return head.next
        else:
            self.removeNode(head, head.next, val)
            return head
             
                
    def removeNode(self, prev, node, val):
        if node != None:
            if node.val == val:
                prev.next = node.next
                self.removeNode(prev, node.next, val)
            else:
                self.removeNode(node, node.next, val)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

s = Solution()
s.removeElements(n1, 6)
n = n1
print n.val
while n.next != None:
    print n.next.val
    n = n.next


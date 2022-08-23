class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    # Iterative T O(n) S O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
            
        return prev
    # Recursive T O(n) S O(n)
    def reverseRecurse(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
    
        newHead = head
        
        if head.next:
            newHead = self.reverseRecurse(head.next)
            head.next.next = head
            
        head.next = None
        
        return newHead
    
def main():
    L = ListNode(5)
    L = ListNode(4,L)
    L = ListNode(3,L)
    L = ListNode(2,L)
    L = ListNode(1,L)
    print(L.val)
    
    s = Solution
    s.reverseList(s,L)
    
main()
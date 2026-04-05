# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWraper():
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        minHeap = []
        for lst in lists:
            heapq.heappush(minHeap, NodeWraper(lst))

        while minHeap:
            node = heapq.heappop(minHeap)
            node = node.node
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minHeap, NodeWraper(node.next))
            
        return dummy.next

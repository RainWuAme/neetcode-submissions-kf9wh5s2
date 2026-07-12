# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        heap = []
        for lst in lists:
            heapq.heappush(heap, NodeWrapper(lst))
        
        res = ListNode(0)
        dummy = res
        while heap:
            cur_node = heapq.heappop(heap)
            dummy.next = cur_node.node
            dummy = dummy.next
            if cur_node.node.next:
                cur_node = cur_node.node.next
                heapq.heappush(heap, NodeWrapper(cur_node))

        return res.next


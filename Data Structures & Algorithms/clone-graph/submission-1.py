"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}

        def bfs(node):
            queue = deque()
            queue.append(node)
            copy = Node(node.val)
            old_to_new[node] = copy
            while queue:
                curr = queue.popleft()
                for nei in curr.neighbors:
                    if nei not in old_to_new:
                        old_to_new[nei] = Node(nei.val)
                        queue.append(nei)
                    old_to_new[curr].neighbors.append(old_to_new[nei])
        bfs(node)

        return old_to_new[node] 
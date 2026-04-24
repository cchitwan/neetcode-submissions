class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        from collections import deque
        queue = deque()
        queue.append(0)
        visited = {0}

        while queue:
            node = queue.popleft()

            for nbh in adj[node]:
                if nbh not in visited:
                    visited.add(nbh)
                    queue.append(nbh)

        return len(visited) == n                    
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            ind[a] += 1
            adj[b].append(a)

        ready = []

        for i in range(numCourses):
            if ind[i] == 0:
                ready.append(i)

        count = 0
        topo=[]
        while ready:
            u = ready.pop()
            count += 1
            topo.append(u)
            for v in adj[u]:
                ind[v] -= 1

                if ind[v] == 0:
                    ready.append(v)
        if len(topo)!=numCourses:
            return []
        return topo
        
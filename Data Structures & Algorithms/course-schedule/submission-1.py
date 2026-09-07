class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        while ready:
            u = ready.pop()
            count += 1

            for v in adj[u]:
                ind[v] -= 1

                if ind[v] == 0:
                    ready.append(v)

        return count == numCourses
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #bfs

        # build the graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for post, pre in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1

        #put the indegree 0 into bfs
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            pre = q.pop()
            count += 1
            for post in graph[pre]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)

        return count == numCourses
            

        

        

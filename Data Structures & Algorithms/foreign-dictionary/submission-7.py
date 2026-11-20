class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def firstDiff(w1, w2):
            if w1 != w2 and w1.startswith(w2):
                return -1, -1
            if w2.startswith(w1):
                return 1, 1
            for p in range( min(len(w1), len(w2))):
                if w1[p] != w2[p]:
                    return w1[p], w2[p]
        
        pre_g = defaultdict(list)

        # find the # unique ch

        indegree = defaultdict(int)
        for w in words:
            for ch in w:
                indegree[ch] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            pre, post = firstDiff(w1, w2)
            if pre == -1:
                return ""
            if pre == 1:
                continue
            pre_g[pre].append(post)
            indegree[post] += 1
        
        q = deque()
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        
        path = ""
        while q:
            pre = q.popleft()
            path += pre
            for post in pre_g[pre]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
        if len(path) != len(indegree):
            return ""
        elif len(indegree) == 1:
            return "".join(indegree.keys())
        else:
            return path

            

        


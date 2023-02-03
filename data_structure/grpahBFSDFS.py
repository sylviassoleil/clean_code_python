class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def BFS(self, s):
        num_v = len(self.graph)
        visited = [False for _ in range(num_v+1)]

        queue = []
        queue.append(s)
        while queue:
            s = queue.pop()
            print(s)
            for v in self.graph[s]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)





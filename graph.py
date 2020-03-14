from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    def add_edge(self, n1, n2):
        self.graph[n1].append(n2)
    def isReachable(self, s, d):
        visited = [False] * (self.v)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            if n == d:
                return True
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

n1 = 2
n2 = 0
if g.isReachable(n1, n2):
    print("there is path from %d to %d "%(n1, n2))
else:
     print("there is no path from %d to %d "%(n1, n2))


n1 = 3
n2 = 3
if g.isReachable(n1, n2):
    print("there is path from %d to %d "%(n1, n2))
else:
     print("there is no path from %d to %d "%(n1, n2))

import copy
from collections import defaultdict
class Node:
    def __init__(self, val):
        self.value = val
        self.has_lib = False
        self.visited = False
        self.edges = []

    def add_edges(self, node):
        self.edges.append(node)


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    # if the node is not connected within 1 edge, build a lib

    has_lib = set([])
    visited = set([])
    graphs = {i: Node(i) for i in range(1, n + 1)}
    cost = 0
    for (from_, to_) in cities:
        graphs[from_].add_edges(graphs[to_])
        graphs[to_].add_edges(graphs[from_])

    for i, n in range(1, n + 1):

        # access to the lib
        if not graphs[i]:
            cost += c_lib
            has_lib.add(i)
        else:
            for k in graphs[i]:
                pass


        visited.add(i)
    return


def dfs(visited, v, graphs):
    if v not in visited:
        visited.add(v)
        for i in graphs[v]:
            dfs(visited, i, graphs)
    return visited


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    # if the node is not connected within 1 edge, build a lib
    # has_access = 0
    if c_road > c_lib:
        return c_lib * n

    graphs = defaultdict(list)
    for (from_, to_) in cities:
        graphs[from_].append(to_)
        graphs[to_].append(from_)


    clusters = []
    visited = set()
    prev_visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue
        visited = dfs(visited, i, graphs)
        clusters.append(visited - prev_visited)
        prev_visited = copy.deepcopy(visited)

    cost = 0
    for cluster in clusters:
        cost += (len(cluster) - 1) * c_road
        cost += c_lib
    return cost


def build_graphs(edges):
    graphs = defaultdict(set)
    for from_, to_ in edges:
        graphs[from_].add(to_)
        graphs[to_].add(from_)
    return graphs


def bfs(n, m, edges, s) -> list:
    # Write your code here
    # todo get the dfs version of this  --- the minimum fare
    weight = 6
    graphs = build_graphs(edges)
    shortest_dis = [-1 for i in range(n + 1)]

    que = [s]
    shortest_dis[s] = 0
    # visited[s] = True
    while que:
        node = que.pop(0) #pop from left
        for i in graphs[node]:
            if shortest_dis[i] == -1:
                que.append(i)
                shortest_dis[i] = shortest_dis[node] + weight

    return [*shortest_dis[1:s], *shortest_dis[s + 1:]]


if __name__ == '__main__':
    pass
    cities = [[1,2], [1,3], [1,4]]
    n = 5
    c_lib, c_road = 6, 1
    c = roadsAndLibraries(n, c_lib, c_road, cities)
    s
    cities = [[1, 7], [1, 5], [2,3]]
    # has_lib = set([])
    # visited = set([])
    n = 6
    graphs = {i: Node(i) for i in range(1, n + 1)}
    cost = 0
    for (from_, to_) in cities:
        graphs[from_].add_edges(graphs[to_])
        graphs[to_].add_edges(graphs[from_])

    cost = 0
    has_lib = set([])
    visited = set([])
    c_lib = 3
    c_road = 2
    has_access=0

    for i, edges in graphs.items():
        # access to the lib
        access = False
        if i in visited:
            continue
        # if not edges:
        #     cost += c_lib
        #     visited.add(i)
        #     has_lib.add(i)
        # else:
        for neighbor in edges:
            if (neighbor in visited):
                cost += c_road
                print(neighbor)
                access = True
                break
        if not access:
            cost += c_lib
            has_lib.add(i)
        visited.add(i)
        has_access += 1


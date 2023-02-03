# bidrectional search

# points to note
# 1. avoid loop
# BFS
import heapq
import sys


def init_graph(g_nodes, g_from, g_to, g_weight):
    graph = [[] for _ in range(g_nodes+1)]
    for f, t, w in zip(g_from, g_to, g_weight):
        graph[f].append((t, w))
        graph[t].append((f, w))
    return graph


def get_current_fare(current, prev_fare):
    return max(current, prev_fare)


def getCost(g_nodes, g_from, g_to, g_weight):
    graph = init_graph(g_nodes, g_from, g_to, g_weight)
    que = [(0, 1)]
    heapq.heapify(que)  # min heap
    visited = [False] * (g_nodes + 1)

    while que:
        cost, node = heapq.heappop(que)
        visited[node] = True
        if node == g_nodes:
            print(cost)
            return

        graph_nodes = graph[node]
        for neighbor, node_cost in graph_nodes:
            if visited[neighbor]: continue
            heapq.heappush(que, (get_current_fare(node_cost, cost), neighbor))

    print('NO PATH EXISTS')


if __name__ == '__main__':
    g_nodes, g_edges = 5, 5
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    inp = '''1 2 60
            3 5 70
            1 4 120
            4 5 150
            2 3 80'''.split('\n')

    for i in range(g_edges):
        input_ = inp[i]
        g_from[i], g_to[i], g_weight[i] = map(int, input_.rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)

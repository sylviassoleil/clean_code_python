''' disjoin-set, union find, aka merge-find '''


# MST kruskal with disjoint list
import heapq


def make_set(g_nodes):
    return [i for i in range(g_nodes + 1)]


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, x, y):
    parent[x] = y
    return parent

def build_edge(g_from, g_to, g_weight):
    ed = []
    heapq.heapify(ed)
    for f, t, w in zip(g_from, g_to, g_weight):
        if f==t:continue
        heapq.heappush(ed, (w, f+t, f, t))
    return ed



def kruskals(g_nodes, g_from, g_to, g_weight):
    parent = make_set(g_nodes)
    edges = build_edge(g_from, g_to, g_weight)
    e, res = 0, 0
    while e < g_nodes - 1:
        w, _, u, v = heapq.heappop(edges)
        xr = find(parent, u)
        yr = find(parent, v)
        if xr != yr:
            e += 1
            res += w
            parent = union(parent, xr, yr)
    return res

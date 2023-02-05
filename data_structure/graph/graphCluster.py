# https://www.hackerrank.com/challenges/journey-to-the-moon/problem


# !/bin/python3
import os

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
from collections import defaultdict


def build_graph(n, astronaut):
    graph = defaultdict(set)
    for from_, to_ in astronaut:
        graph[from_].add(to_)
        graph[to_].add(from_)
    return graph


def dfs(visited, i, graph):
    visited.add(i)
    for k in graph[i]:
        if k not in visited:
            dfs(visited, k, graph)
    return visited


def journeyToMoon(n, astronaut):
    # Write your code here
    graph = build_graph(n, astronaut)
    cluster = {}
    pairs = 0
    for i in range(n):
        if i not in cluster:
            visited = dfs(set(), i, graph)
            connected_len_ = len(visited)
            for i in visited:
                cluster.update({i: connected_len_})
        unconnected = n - cluster[i]
        # print(i, visited)
        if not unconnected:
            return 0
        pairs += unconnected
    return pairs // 2


def journeyToMoon(n, astronaut):
    cluster = [set([]) for _ in range(n)]
    for from_, to_ in astronaut:
        cluster[from_].add(to_)
        cluster[to_].add(from_)
        connected = cluster[from_].union(cluster[to_])
        for i in connected:
            cluster[i] = connected

    # print(cluster)
    cluster = set([tuple(i) for i in cluster])
    # print(cluster)
    same_country_paris = 0
    for c in cluster:
        same_country_paris += len(c) * (len(c) - 1)
    return (n * (n - 1) - same_country_paris) // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

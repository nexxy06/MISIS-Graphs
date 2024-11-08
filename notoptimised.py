class SimpleDisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u):
        while u != self.parent[u]:
            u = self.parent[u]
        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]


def kruskal(n, edges):
    ds = SimpleDisjointSet(n)
    mst = []
    total_weight = 0

    # сортируем рёбра по весу
    edges.sort(key=lambda edge: edge[2])

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# пример использования
n = 6
edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 5),
    (2, 4, 9),
    (3, 4, 7),
    (3, 5, 3),
    (4, 5, 1)
]

mst, total_weight = kruskal(n, edges)
print("Минимальное остовное дерево:", mst)
print("Общий вес:", total_weight)

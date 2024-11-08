class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
    # для теста

    def connected(self, u, v):
        return self.find(u) == self.find(v)


if __name__ == "__main__":
    ds = DisjointSet(10)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(1, 4)
    print(ds.find(2))  # корень множества содержащего элемент 2
    print(ds.find(3))  # корень множества содержащего элемент 3

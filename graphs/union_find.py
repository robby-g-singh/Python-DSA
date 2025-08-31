class UnionFind:
    def __init__(self, n):  # NOTE: for inputs of pre-defined arbitrary values - use hash maps for parent and ranks!
        # Initially, each node is its own parent
        self.parent = [i for i in range(n)]
        # Rank helps to keep the tree shallow
        self.rank = [1] * n

    def find(self, x):
        # path compression: point every node directly to the root
        # recursive call to find the parent of x; if the parent of x is not x
        if self.parent[x] != x:
            # recursive call to re-write the parent of x so that in the future it's constant time lookup
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)  # parent of x
        root_y = self.find(y)  # parent of y

        if root_x == root_y:
            return False  # already in the same set; share the same parent

        # union by rank: attach smaller tree under bigger tree
        if self.rank[root_x] > self.rank[root_y]:  # if the rank of parent x is greater, meaning it is a taller tree,
            # then add root_y's tree to root_x
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            # otherwise, the entire tree of root_x will be attached to root_y
            self.parent[root_x] = root_y
        else:
            # if they're the same, or 0 to start with, then by default y will be attached to x and x's rank is
            # incremented for every component attached
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

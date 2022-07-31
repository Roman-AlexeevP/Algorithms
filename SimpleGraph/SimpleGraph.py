class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        if v is None:
            return False
        vertex = Vertex(v)
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = vertex
                return True

        return False

    def RemoveVertex(self, v):
        if v >= self.max_vertex or self.vertex[v] is None:
            return False
        if self.vertex[v] is None:
            return False
        self.vertex[v] = None
        for i in range(self.max_vertex):
            for j in range(self.max_vertex):
                if j == v or i == v:
                    self.m_adjacency[i][j] = 0
        return True

    def IsEdge(self, v1, v2):
        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return False
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        is_edge = self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1
        return is_edge

    def AddEdge(self, v1, v2):
        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return False
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1, v2):
        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return False
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        pass

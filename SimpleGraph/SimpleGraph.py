class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


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

    def DepthFirstSearch(self, VFrom, VTo):
        if VFrom is None or VTo is None:
            return []
        if VFrom >= self.max_vertex or VTo >= self.max_vertex:
            return []
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        visited_vertex_stack = []
        visited_vertex_stack.append(self.vertex[VFrom])

        while len(visited_vertex_stack) > 0:
            vertex = visited_vertex_stack[-1]
            vertex.Hit = True

            if self.m_adjacency[VFrom][VTo] == 1:
                visited_vertex_stack.append(self.vertex[VTo])
                return visited_vertex_stack

            for v in range(len(self.m_adjacency[VFrom])):
                if self.m_adjacency[VFrom][v] == 1 and not self.vertex[v].Hit:
                    VFrom = v
                    visited_vertex_stack.append(self.vertex[VFrom])
                    break
            else:
                visited_vertex_stack.pop()

        return []


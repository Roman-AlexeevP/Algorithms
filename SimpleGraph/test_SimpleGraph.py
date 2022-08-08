from SimpleGraph import *


def test_AddVertex():
    test_value = 1
    graph = SimpleGraph(5)
    graph.AddVertex(test_value)
    vertex = next(v for v in graph.vertex if v is not None)
    assert vertex is not None
    assert vertex.Value == test_value


def test_IsEdge():
    graph = SimpleGraph(5)

    for i in range(3):
        graph.AddVertex(i)
    v1 = 0
    v2 = 1
    assert not graph.IsEdge(v1, v2)
    graph.m_adjacency[v1][v2] = 1
    graph.m_adjacency[v2][v1] = 1
    assert graph.IsEdge(v1, v2)


def test_AddEdge():
    graph = SimpleGraph(5)

    for i in range(3):
        graph.AddVertex(i)
    v1 = 0
    v2 = 1
    assert not graph.IsEdge(v1, v2)
    graph.AddEdge(v1, v2)
    assert graph.IsEdge(v1, v2)


def test_RemoveEdge():
    graph = SimpleGraph(5)

    for i in range(3):
        graph.AddVertex(i)
    v1 = 0
    v2 = 1
    graph.AddEdge(v1, v2)
    graph.RemoveEdge(v1, v2)
    assert not graph.IsEdge(v1, v2)


def test_RemoveVertex():
    graph = SimpleGraph(5)

    for i in range(3):
        graph.AddVertex(i)
    v = 0
    graph.RemoveVertex(v)
    assert graph.vertex[v] is None
    assert all(list(filter(lambda x: x[v] == 0, graph.m_adjacency)))

def test_DFS():
    graph = SimpleGraph(5)
    for i in range(4):
        graph.AddVertex(i)
    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(1, 3)
    graph.AddVertex(5)
    assert graph.DepthFirstSearch(0, 2) == [graph.vertex[v] for v in range(3)]
    assert graph.DepthFirstSearch(0, 3) == [graph.vertex[0], graph.vertex[1], graph.vertex[3]]
    assert graph.DepthFirstSearch(2, 3) == [graph.vertex[2], graph.vertex[1], graph.vertex[3]]
    assert graph.DepthFirstSearch(1, 4) == []
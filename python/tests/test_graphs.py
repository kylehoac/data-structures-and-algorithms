import pytest
from code_challenges.graphs.graphs import Graph, Vertex

def test_exists():
    assert Graph

def test_add_node():
    graph = Graph()
    actual = graph.add_node('1')
    expected_value = '1'
    assert actual.value == expected_value

def test_add_edge():
    graph = Graph()
    vertex1 = graph.add_node('1')
    vertex2 = graph.add_node('2')
    graph.add_edge(vertex1, vertex2)
    has_edge = graph.get_neighbors(vertex1)
    assert len(has_edge) == 1

def test_get_nodes_one():
    graph = Graph()
    graph.add_node('1')
    actual = graph.get_nodes()
    expected = 1
    assert len(actual) == expected
    assert isinstance(actual[0], Vertex)
    assert actual[0].value == '1'

def test_get_nodes():
    graph = Graph()
    graph.add_node('1')
    graph.add_node('1')
    graph.add_node('1')
    actual = graph.get_nodes()
    expected = 3
    assert len(actual) == expected
    assert actual[0].value == '1'
    assert actual[1].value == '1'
    assert actual[2].value == '1'

def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_node('1')
    vertex2 = graph.add_node('2')
    graph.add_edge(vertex1, vertex2, 5)
    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 1
    single_edge = neighbors[0]
    assert single_edge.vertex.value == '2'
    assert single_edge.weight == 5

def test_get_neighbors_solo():
    graph = Graph()
    spam_vertex = graph.add_node('1')
    graph.add_edge(spam_vertex, spam_vertex)
    neighbors = graph.get_neighbors(spam_vertex)
    assert len(neighbors) == 1
    single_edge = neighbors[0]
    assert single_edge.vertex.value == '1'
    assert single_edge.weight == 0

def test_size():
    graph = Graph()
    graph.add_node('1')
    graph.add_node('2')
    actual = graph.size()
    expected = 2
    assert actual == expected

def test_size_returns_empty():
    graph = Graph()
    actual = graph.size()
    expected = 0
    assert actual == expected

def test_business_trip_exists():
    assert Graph.business_trip
def test_business_trip_is_possible():
    graph = Graph()
    vertex1 = graph.add_node('Los Angeles')
    vertex2 = graph.add_node('Denver')
    vertex3 = graph.add_node('New York')
    graph.add_edge(vertex1, vertex2, 100)
    graph.add_edge(vertex2, vertex3, 275)
    city_lst = [vertex1, vertex2, vertex3]
    actual = graph.business_trip(graph, city_lst)
    expected = True, 375
    assert actual == expected
def test_business_trip_is_possible_2():
    graph = Graph()
    vertex1 = graph.add_node('Los Angeles')
    vertex2 = graph.add_node('Denver')
    vertex3 = graph.add_node('New York')
    vertex4 = graph.add_node('Miami')
    graph.add_edge(vertex1, vertex2, 100)
    graph.add_edge(vertex2, vertex3, 275)
    graph.add_edge(vertex3, vertex4, 200)
    city_lst = [vertex1, vertex2, vertex3, vertex4]
    actual = graph.business_trip(graph, city_lst)
    expected = True, 575
    assert actual == expected
def test_business_trip_fail():
    graph = Graph()
    vertex1 = graph.add_node('Los Angeles')
    vertex2 = graph.add_node('Denver')
    vertex3 = graph.add_node('New York')
    graph.add_edge(vertex1, vertex2, 100)
    graph.add_edge(vertex2, vertex3, 275)
    city_lst = [vertex1, vertex3]
    actual = graph.business_trip(graph, city_lst)
    expected = True, 375
    assert actual != expected
def test_has_one_item():
    graph = Graph()


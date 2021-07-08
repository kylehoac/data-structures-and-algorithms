from code_challenges.depth_first_graph.depth_first_graph import depth_traversal, Stack, Node
from code_challenges.graphs.graphs import Graph, Vertex
def test_depth_traversal_exists():
    assert depth_traversal
def test_depth_traversal_one():
    graph = Graph()
    boston = graph.add_node('Boston')
    seattle = graph.add_node('Seattle')
    la = graph.add_node('LA')
    sf = graph.add_node('SF')
    chi = graph.add_node('CHI')
    ny = graph.add_node('NY')
    graph.add_edge(boston, ny, 82)
    graph.add_edge(boston, chi, 90)
    graph.add_edge(ny, chi, 42)
    graph.add_edge(ny, seattle, 200)
    graph.add_edge(ny, la, 225)
    graph.add_edge(ny, sf, 230)
    graph.add_edge(chi, seattle, 175)
    graph.add_edge(seattle, sf, 85)
    graph.add_edge(sf, la, 85)
    actual = depth_traversal(boston, graph)
    expected = [boston, chi, seattle, sf, la, ny]
    assert actual == expected
def test_depth_traversal_two():
    graph = Graph()
    city = graph.add_node('Boston')
    town = graph.add_node('Seattle')
    place = graph.add_node('LA')
    graph.add_edge(city, town, 82)
    graph.add_edge(town, place, 90)
    graph.add_edge(city, place, 42)
    actual = depth_traversal(city, graph)
    expected = [city, place, town]
    assert actual == expected

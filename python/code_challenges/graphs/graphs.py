class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start, end, weight=0):
        edge = Edge(end, weight)
        self.adjacency_list[start].append(edge)

    def get_neighbors(self, vertex):
        # return self.adjacency_list[vertex]
        return self.adjacency_list.get(vertex,[])

    @staticmethod
    def business_trip(graph, city_lst):
        cost = 0

        if not city_lst:
            return False

        for i, city in enumerate(city_lst):
            if i+1 == len(city_lst):
                return True, cost

            for neighbors in graph.get_neighbors(city):

                if city_lst[i+1] != neighbors.vertex:
                    return False, 0

                if city_lst[i+1] == neighbors.vertex:
                    cost += neighbors.weight
                    break
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

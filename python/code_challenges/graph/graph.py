
class Graph:

    def __init__(self):
        self.vertices_list = []

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self.vertices_list:
            self.vertices_list.append(vertex)
            return vertex

    def add_edge(self, v1, v2, weight=1):
        if v1 in self.vertices_list and v2 in self.vertices_list:
            edge = Edge(v2, weight)
            v1.adjacent_list.append([v2, edge])
        else:
            raise(KeyError)

    def get_nodes(self):
        return self.vertices_list

    def get_neighbors(self, vertex):
        neighbors = []
        for item in self.vertices_list:
            if item.value == vertex.value:
                # print("hello")
                # print(item.adjacent_list)
                for edges in item.adjacent_list:
                    # print(edges)
                    neighbors.append(edges[1])
        return neighbors

    def size(self):
        return len(self.vertices_list)

class Vertex:
    '''
    Vertex represents the individual Nodes inside the graph.
    The attribute value represents the stored data.
    The list of neighbors attribute represents the vertices with which exists a connection.
    '''
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


if __name__ == '__main__':
    g=Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    orange = g.add_node("orange")
    strawberry = g.add_node("strawberry")
    g.add_edge(apple, strawberry, 10)
    g.add_edge(apple, orange, 6)
    g.add_edge(apple, banana, 5)
    print([edge.vertex.value for edge in g.get_neighbors(apple)])

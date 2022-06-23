import abc
import numpy as np


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class AdjancencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def is_valid_vertex(self, v):
        return (v < self.num_vertices) and (v >= 0)

    def add_edge(self, v1, v2, weight=1):
        if (not self.is_valid_vertex(v1)) or (not self.is_valid_vertex(v2)):
            raise Exception("Invalid vertex supplied")
        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        ret = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                # Path exists
                ret.append(i)
        return ret

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def get_indegree(self, v):
        ret = []
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                # Path exists
                ret.append(i)
        return len(ret)

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "--->", v)

class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id != v:
            self.adjacency_set.add(v)

    def get_adjacency_vertices(self):
        return sorted(self.adjacency_set)


class AdjancencySetGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        self.vertex_list = []
        for i in range(self.num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if weight != 1:
            raise Exception("invalid weight, only 1 allowed")
        self.vertex_list[v1].add_edge(v2)
        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        return self.vertex_list[v].get_adjacency_vertices()

    def get_edge_weight(self, v1, v2):
        return 1

    def get_indegree(self, v):
        counter = 0
        for i in range(self.num_vertices):
            if v in self.vertex_list[i].get_adjacency_vertices():
                counter += 1
        return counter

    def display(self):
        for i in range(self.num_vertices):
            for item in self.vertex_list[i].get_adjacency_vertices():
                print(i, "--->", item)


if __name__ == "__main__":
    g = AdjancencyMatrixGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print("{} is Adajcent to {}".format(i, g.get_adjacent_vertices(i)))

    g.display()

    print("--------------------------------------------------------------------------------")

    g = AdjancencySetGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print("{} is Adajcent to {}".format(i, g.get_adjacent_vertices(i)))

    g.display()

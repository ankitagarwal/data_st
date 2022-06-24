from graphs.graph import *
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


def bfs(graph, start):
    q = Queue()
    q.enqueue(start)
    predecessor = {start: None}
    while not q.is_empty():
        node = q.dequeue()
        # print(g.get_adjacency_vertices())
        for n in g.get_adjacent_vertices(node):
            if n not in predecessor:
                q.enqueue(n)
                predecessor[n] = node
    print(predecessor)
    return None

class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return not self.items


def dfs(g, start):
    s = Stack()
    s.push(start)
    predecessors = {start: None}
    while not s.is_empty():
        node = s.pop()
        # print("processing ", node)
        for n in g.get_adjacent_vertices(node):
            if n not in predecessors:
                s.push(n)
                predecessors[n] = node

    print(predecessors)
    return None



if __name__ == "__main__":
    g = AdjancencyMatrixGraph(9)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)
    bfs(g, 2)
    dfs(g, 0)

    print("-----------------------------------------------")
    g = AdjancencyMatrixGraph(9, True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)
    bfs(g, 0)
    dfs(g, 0)


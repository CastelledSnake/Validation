from abc import ABC
from collections import deque

# Nettoyer le bazar, pour laisser le duck typing ?
# Ou bien trouver une manière de garder le static typing ?

Node = int
HanoiNode = tuple[int, ...]


class RootedGraph(ABC):
    def roots(self):
        """
        returns the root of the graph
        :return: the roots
        """
        pass

    def neighbours(self, node):
        """
        returns the children nodes of the graph
        :param node: the node we want to get the children from.
        :return: the list of the node's children.
        """
        pass


class ParentTracer(RootedGraph):
    def __init__(self, rg):
        self.rg = rg
        self.parents = {}

    def roots(self):
        roots = self.rg.roots()
        for node in roots:
            self.parents[node] = []
        return roots

    def neighbours(self, node):
        neighbours = self.rg.neighbours(node)
        for neighbour in neighbours:
            if neighbour not in self.parents:
                self.parents[neighbour] = [node]
        return neighbours

    def get_trace(self, solution):
        trace = [solution]
        parent = self.parents.get(solution)
        while parent is not None and len(parent) > 0:
            parent = parent[0]
            trace.append(parent)
            parent = self.parents[parent]
        return trace


"""
def bfs_search(rg: RootedGraph, query: typing.Callable[[Node], bool]):
    visited = set([rg.roots()])
    queue = deque([rg.roots()])

    if query(rg.roots()):
        return (rg.roots(), visited)

    while queue:
        vertex = queue.popleft()
        for neighbour in rg.neighbours(vertex):
            if neighbour not in visited:
                if query(neighbour):
                    return (neighbour, visited)
                visited.add(neighbour)
                queue.append(neighbour)

    return (None, visited)
"""


# def bfs_search(rg: RootedGraph, query: typing.Callable[[Node], bool]):
def bfs_search(rg, query):
    visited = set()
    queue = deque()
    i = True

    while queue or i:
        if i:
            neighbours = rg.roots()
            i = False
        else:
            vertex = queue.popleft()
            neighbours = rg.neighbours(vertex)

        for neighbour in neighbours:
            if neighbour not in visited:
                if query(neighbour):
                    return neighbour, visited
                visited.add(neighbour)
                queue.append(neighbour)
    return None, visited

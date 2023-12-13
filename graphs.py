from abc import ABC
from collections import deque
import typing

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


class HanoiGraph(RootedGraph):
    def __init__(self, disks: int, root: HanoiNode):
        self.graph = {}
        self.disks = disks
        self.root = root
        self.solution = tuple(2 for i in range(disks))

    def roots(self):
        """
        returns the root of the graph
        :return: the roots
        """
        return [self.root]

    def is_solution(self, n: HanoiNode) -> bool:
        """
        returns iff the node is final
        :param n: the node to evaluate
        :return: boolean
        """
        return n == self.solution

    def neighbours(self, node: HanoiNode) -> list[HanoiNode]:
        """
        determines the list of neighbours of the HanoiNode given.
        :param node: a HanoiNode instance.
        :return: a list of children.
        """
        neighbours = []
        stack_finalised = [False, False, False]
        for disk, stack in enumerate(node):
            if stack_finalised[stack]:
                continue
            # Early-exit, might not be
            # if all(stack_finalised):
            #     break
            stack_finalised[stack] = True

            # Find possible moves
            if not stack_finalised[0]:
                neighbour = list(node)
                neighbour[disk] = 0
                neighbours.append(tuple(neighbour))
            if not stack_finalised[1]:
                neighbour = list(node)
                neighbour[disk] = 1
                neighbours.append(tuple(neighbour))
            if not stack_finalised[2]:
                neighbour = list(node)
                neighbour[disk] = 2
                neighbours.append(tuple(neighbour))

        #print("node", node, neighbours)
        return neighbours


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


if __name__ == '__main__':
    # rg = RootedGraph({1: [2, 3], 2: [3, 4], 3: [], 4: []}, 1)
    # def a(n: Node) -> bool:
    #     return n == 2

    # def b(n: Node) -> bool:
    #     return n == 5

    # print(bfs_search(rg, a))
    # print(bfs_search(rg, b))

    # hanoi = HanoiGraph(2, (0, 0))
    hanoi = HanoiGraph(3, (0, 0, 0))
    parent_tracer = ParentTracer(hanoi)
    t, k = bfs_search(parent_tracer, hanoi.is_solution)
    print(t, k)
    parent_tracer.get_trace(t)
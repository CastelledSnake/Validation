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

        # print("node", node, neighbours)
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


class ABNode:
    def __init__(self, name, guards, actions):
        self.name: str = name
        self.guards = guards
        self.actions = actions


class AliceAndBob(RootedGraph):
    def __init__(self):
        # The protagonists (or their dog, or their cat, or whatever dangerous thing that should not be in a garden.
        self.alice = {}
        self.bob = {}
        # Initially, nobody is in the garden.
        self.turn = 0
        # Alice and Bob don't want to go in the garden, initially.
        self.fa = False
        self.fb = False
        # Initialising all nodes
        self.init_a = ABNode("Initial_Alice", "", "fA = True, turn = 2")
        self.wait_a = ABNode("Alice_Wait", "turn == 1 || fB == False", "")
        self.critic_a = ABNode("Critical_Alice", "", "fA = False")
        self.init_b = ABNode("Initial_Bob", "", "fB = True, turn = 1")
        self.wait_b = ABNode("Alice_Bob", "turn == 2 || fA == False", "")
        self.critic_b = ABNode("Critical_Bob", "", "fB = False")

    def filling(self):
        """
        Fills alice and bob
        :return: None
        """
        self.alice = {
            self.init_a: [self.wait_a],
            self.wait_a: [self.critic_a],
            self.critic_a: [self.init_a]
        }
        self.bob = {
            self.init_b: [self.wait_b],
            self.wait_b: [self.critic_b],
            self.critic_b: [self.init_b]}

    def roots(self):
        return [self.init_a, self.init_b]

    def neighbours(self, node):
        if node in self.alice:
            return self.alice[node]
        elif node in self.bob:
            return self.bob[node]
        else:
            raise ValueError(f"Node {node} is not in alice or bob")
    # IDEA : Define one function per action to perform, and per guard to test (8 of them in total).


class Semantics(ABC):
    def initial(self):
        """
        returns the initial states of the graph.
        :return: a list of nodes.
        """
        pass

    def actions(self, node):
        """
        returns the functions that a node can compute
        :param node: a node
        :return: a list of functions.
        """
        pass

    def execute(self, action, node):
        """
        executes an action on the node
        :param action: a function
        :param node: a node
        :return: action(node)
        """
        pass


class OneBitClock(Semantics):
    def initial(self):
        return [0, 1]

    def actions(self, c):
        a = []
        if c == 1:
            a.append(lambda x: [0])
        elif c == 0:
            a.append(lambda x: [1])
        return a

    def execute(self, a, c):
        return a(c)
    

if __name__ == "__main__":
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
    trace = parent_tracer.get_trace(t)
    print(trace)

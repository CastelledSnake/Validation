from collections import deque
import typing

# Nettoyer le bazar, pour laisser le duck typing ?
# Ou bien trouver une manière de garder le static typing ?


Node = int
HanoiNode = tuple[int, ...]

class RootedGraph:
    def __init__(self, graph: dict[Node, list[Node]], root: Node):
        self.graph = graph
        # self.root = [1]
        self.root = root

    def roots(self) -> Node:
        return self.root

    def neighbours(self, node: Node) -> list[Node]:
        return self.graph[node]


# def bfs_search(rg: RootedGraph, query: typing.Callable[[Node], bool]):
#     visited = set([rg.roots()])
#     queue = deque([rg.roots()])

#     if query(rg.roots()):
#         return (rg.roots(), visited)

#     while queue:
#         vertex = queue.popleft()
#         for neighbour in rg.neighbours(vertex):
#             if neighbour not in visited:
#                 if query(neighbour):
#                     return (neighbour, visited)
#                 visited.add(neighbour)
#                 queue.append(neighbour)

#     return (None, visited)


class HanoiGraph(RootedGraph):
    def __init__(self, disks: int, root: HanoiNode):
        self.graph = {}
        self.disks = disks
        self.root = root
        self.solution = tuple(2 for i in range(disks))

    def roots(self) -> HanoiNode:
        return self.root

    def is_solution(self, n: HanoiNode) -> bool:
        return n == self.solution

    def neighbours(self, node: HanoiNode) -> list[HanoiNode]:
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

        print("node", node, neighbours)
        return neighbours


# def bfs_search(rg: RootedGraph, query: typing.Callable[[Node], bool]):
def bfs_search(rg: HanoiGraph, query: typing.Callable[[HanoiNode], bool]):
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
    print(bfs_search(hanoi, hanoi.is_solution))
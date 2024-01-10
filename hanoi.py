from graphs import *

# Nettoyer le bazar, pour laisser le duck typing ?
# Ou bien trouver une manière de garder le static typing ?

Node = int
HanoiNode = tuple[int, ...]


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

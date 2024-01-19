from abc import ABC


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

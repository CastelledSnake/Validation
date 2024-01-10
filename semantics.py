from abc import ABC


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

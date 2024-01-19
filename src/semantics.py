from abc import ABC


class Semantics(ABC):
    def initial(self):
        """
        returns the initial states of the graph.
        :return: a list of nodes.
        """
        pass

    def actions(self, configuration):
        """
        returns the functions that a node can compute
        :param node: a node
        :return: a list of functions.
        """
        pass

    def execute(self, action, configuration):
        """
        executes an action on the node
        :param action: a function
        :param node: a node
        :return: action(node)
        """
        return action(configuration)


class Sem2RG:
    pass

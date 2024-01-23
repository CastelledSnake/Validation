from abc import ABC, abstractmethod

from graph.rooted_graph import RootedGraph


class Semantics(ABC):
    @abstractmethod
    def initial(self):
        """
        returns the initial states of the graph.
        :return: a list of nodes.
        """
        pass

    @abstractmethod
    def actions(self, configuration):
        """
        returns the functions that a node can compute
        :param node: a node
        :return: a list of functions.
        """
        pass

    @abstractmethod
    def execute(self, action, configuration):
        """
        executes an action on the node
        :param action: a function
        :param node: a node
        :return: action(node)
        """
        return action(configuration)


class Sem2RG(RootedGraph):
    # TODO: implement this
    pass

from abc import ABC, abstractmethod
from typing import Iterable


class RootedGraph(ABC):
    @abstractmethod
    def roots(self) -> Iterable:
        """
        returns the root of the graph
        :return: the roots
        """
        pass

    @abstractmethod
    def neighbours(self, node) -> Iterable:
        """
        returns the children nodes of the graph
        :param node: the node we want to get the children from.
        :return: the list of the node's children.
        """
        pass

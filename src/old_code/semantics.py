from abc import ABC, abstractmethod
from typing import Callable

from graph.rooted_graph import RootedGraph


class Semantics(ABC):
    @abstractmethod
    def initial(self) -> list:
        """
        returns the initial states of the graph.
        :return: a list of nodes.
        """
        pass

    @abstractmethod
    def actions(self, configuration) -> list[Callable]:
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


class SemToRG(RootedGraph):
    """
    Permet de déterminer le graphe associé à une sémantique.
    """

    def __init__(self, semantics: Semantics):
        self.semantics = semantics

    def roots(self):
        """
        Renvoie l'ensemble des nœuds-racines du graphe.
        :return: Les nœuds-racines du graphe
        """
        return self.semantics.initial()

    def neighbours(self, node):
        """
        Renvoie les voisins d'un nœud.
        :param node: Un nœud.
        :return: Une liste des nœuds voisins du nœud en argument.
        """
        neighbours = []
        actions = self.semantics.actions(node)
        for action in actions:
            neighbours.extend(self.semantics.execute(node, action))
        return neighbours

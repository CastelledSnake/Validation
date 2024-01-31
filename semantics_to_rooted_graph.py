from graphs import RootedGraph


class SemToRG(RootedGraph):
    """
    Permet de déterminer le graphe associé à une sémantique.
    """
    def __init__(self, semantics):
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
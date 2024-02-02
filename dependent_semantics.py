from abc import ABC
from copy import deepcopy

from soup_language import Piece, SoupSpec, SoupConfiguration


class DependentSemantics(ABC):
    def initials(self):
        pass

    def actions(self, inpt, config):
        pass

    def execute(self, action, inpt, config):
        pass


class DependentSoupSemantics(DependentSemantics):
    def __init__(self, soup: SoupSpec):
        self.soup = soup

    def initials(self):
        self.soup.initial()

    def actions(self, inpt, source):
        """
        Retourne les pièces dont la garde est vérifiée.
        :param inpt:
        :param source:
        :return: Une liste de Pieces
        """
        return filter(lambda piece: piece.guards(inpt, source), self.soup.pieces)

    def execute(self, piece: Piece, inpt, source):
        """
        Retourne une copie des actions effectuées par une Piece (on ne veut pas parcourir le graphe effectivement).
        :param piece: La Piece.
        :param inpt:
        :param source:
        :return: Les actions associées.
        """
        src = deepcopy(source)
        inp = deepcopy(inpt)
        return piece.action(inp, src)

# Avec ça, on va pouvoir vérifier les 3 types de propriétés sur A&B :
#   Safety (avec bfs, uniquement).
#   Liveness avec les Soup.
#   L + S avec les boucles.

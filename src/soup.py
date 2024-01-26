from typing import Callable
from src.semantics import Semantics


class SoupConfiguration:
    """Soup configuration
    Classe définissant la configuration de la soupe.
    """

    def __init__(self):
        pass


class SoupSpec:
    """Soup specification
    Classe définissant la soupe de pièces.
    Capable de contenir des pièces.
    Et permet de vérifier que les gardes des pièces correspondent à la configuration qu'on donne à SoupSpec.
    """

    def __init__(self):
        pass


class SoupSemantic(Semantics):
    """Semantique de la soupe
    Classe définissant la semantique de la soupe.

    Sémantique = ensemble des expressions d'un langage.

    Cette classe permet d'itérer sur l'ensemble des pièces d'une SoupSpec.

    A chaque étape, la classe demande à la SoupSpec les pièces possibles pour la configuration donnée.
    i.e. les états vers lesquels on peut aller depuis la configuration donnée.
    Une fois l'ensemble reçu, applique une pièce.
    => se base sur Sem2RG et donc bfs pour déterminer la pièce suivante.
    (à vérifier)
    """

    def initial(self):
        # TODO: implement this
        return NotImplementedError

    def actions(self, configuration: SoupConfiguration):
        pieces = (
            configuration.pieces
        )  # TODO: A verifier => récup les pieces à tout prix !
        for piece in pieces:
            if piece.cond(configuration):
                return piece.lbda(configuration)


class Piece:
    """Piece
    La Piece décrit comment passer d'un état (noeud) A à un état B. C'est donc une combinaison (Gardes, Actions).
    Mais on ajoute aussi un composant dans la garde, pour savoir si je suis dans l'état A au départ (state == A),
        et il y a dans l'action de la Piece, le changement d'état vers B (state = B).
    A chaque étape, la sémantique regarde quelles sont les pièces dont la garde vérifie les conditions présentes.
    """

    def __init__(self, name: str, cond, lbda) -> None:
        self.name = name
        self.cond = "soemthing"
        self.lbda = "lambda syntax"
        # TODO: implement this

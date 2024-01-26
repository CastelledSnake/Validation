from typing import Callable, List
from semantics_to_rooted_graph import *


class SoupConfiguration:
    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, SoupConfiguration):
            return self.__hash__() == __value.__hash__()
        return NotImplemented

    def __repr__(self) -> str:
        return "SoupConfiguration"


class Piece:
    """
    La Piece décrit comment passer d'un état (noeud) A à un état B. C'est donc une combinaison (Gardes, Actions).
    Mais on ajoute aussi un composant dans la garde, pour savoir si je suis dans l'état A au départ (state == A),
        et il y a dans l'action de la Piece, le changement d'état vers B (state = B).
    A chaque étape, la sémantique regarde quelles sont les pièces dont la garde vérifie les conditions présentes.
    """

    def __init__(self, name: str, guard: Callable[[SoupConfiguration], bool] = lambda c: True, action: Callable[[SoupConfiguration], None] = lambda c: None):
        self.name: str = name
        self.guard = guard
        self.action = lambda c: None

    def enabled(self, config: SoupConfiguration):
        return self.guard(config)

    def execute(self, config: SoupConfiguration):
        return self.action(config)


class SoupSpec:
    def __init__(self, initial_configs: List[SoupConfiguration], pieces: List[Piece]):
        self.configs = initial_configs
        self.pieces = pieces

    def enabled_pieces(self, config: SoupConfiguration) -> List[Piece]:
        return list(filter(lambda p: p.enabled(config), self.pieces))


class SoupSemantics:
    def __init__(self, spec: SoupSpec):
        self.spec = spec

    def initial(self):
        self.spec.initial()  # type: ignore

    def actions(self, config: SoupConfiguration):
        self.spec.enabled_pieces(config)

    def execute(self, action, config):
        return action.execute(config)


class OBCConfig(SoupConfiguration):
    def __init__(self, init_clock: int):
        self.clock = init_clock

    def __hash__(self):
        return hash(self.clock)

    def __repr__(self):
        return f"OBCConfig(clock={self.clock})"


if __name__ == "__main__":
    p1 = Piece("1->0")
    p2 = Piece("0->1")
    soup = SoupSpec([OBCConfig(0)], [p1, p2])
    soup_sem = SoupSemantics(soup)
    # s = Sem2RG(soup_sem)


# A faire : On a """fait""" une soupconfig de OneBitClock, il faut en faire une pour AliceetBob et Hanoi.

# Notes prises le 19/01/24:
#                                 predicate-|.
# Soup->SoupSemantic->Sem2RG->ParentTracer->bfs->getTrace
#                                  |--------|^
#
# Il nous manque un langage de propriétés qui nous permet de tester toutes les fonctions calculables.
# Pour faire le lien entre la SoupSemantic et la Semantic2RG.
# Il nous faudra aussi un produit synchrone entre la SoupSemantic et le langage qu'on va créer.
#       Il calculera l'intersection d'un modèle et la négation d'une propriété à tester.
# Enfin, il nous manque un Det Cycle : un truc par-dessus le bfs pour détecter les mauvaises boucles d'exécution.

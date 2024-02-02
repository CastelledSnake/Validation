from abc import ABC
from typing import Callable, List
from semantics_to_rooted_graph import *
from copy import deepcopy


class SoupConfiguration(ABC):
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
    La Piece décrit comment passer d'un état (nœud) A à un état B. C'est donc une combinaison (Gardes, Actions).
    Mais on ajoute aussi un composant dans la garde, pour savoir si on est dans l'état A au départ (state == A),
        et il y a dans l'action de la Piece, le changement d'état vers B (state = B).
        C'est ainsi un ensemble (nœud_départ, gardes, actions, nœud_arrivée).
    """
    def __init__(
        self,
        name: str,
        guard: Callable[[SoupConfiguration], bool] = lambda c: True,
        action: Callable[[SoupConfiguration], None] = lambda c: None,
    ):
        self.name: str = name
        self.guards = guard  # guard
        self.action = action  # lambda c: None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Piece {self.name}({self.guards}) --> {self.action}"

    def enabled(self, config):  # Possible type : SoupConfiguration
        return self.guards(config)

    def execute(self, config):  # Possible type : SoupConfiguration
        return [self.action(deepcopy(config))]


class SoupSpec:
    """
    Prend une liste de configuration(s) initiale(s) et une liste de Pieces.
    Son rôle est de comparer la/les configuration(s) initiale(s) et les gardes des Pieces.
    """

    def __init__(self, initial_configs: List[SoupConfiguration], pieces: List[Piece]):
        self.configs = initial_configs
        self.pieces = pieces

    def initial(self):
        """
        Renvoie la présente configuration.
        :return: Une configuration.
        """
        return self.configs

    def enabled_pieces(self, config: SoupConfiguration) -> List[Piece]:
        """
        La sémantique regarde quelles sont les pièces dont la garde vérifie la configuration donnée.
        :param config: La configuration.
        :return: La liste des Pieces concordantes.
        """
        return list(filter(lambda p: p.enabled(config), self.pieces))


class SoupSemantics:
    """
    Permet de déterminer la sémantique d'une SoupSpecification.
    """

    def __init__(self, spec: SoupSpec):
        self.spec = spec

    def initial(self):
        return self.spec.initial()  # type: ignore

    def actions(self, config: SoupConfiguration):
        return self.spec.enabled_pieces(config)

    def execute(self, action, config: SoupConfiguration):
        return action.execute(config)


class OBCConfig(SoupConfiguration):
    """
    Mise en œuvre d'une configuration d'une horloge binaire (One Bit Clock).
    """

    def __init__(self, init_clock: int):
        self.clock = init_clock

    def __repr__(self):
        return f"OBCConfig(clock={self.clock})"

    def __hash__(self):
        return hash(self.clock)

    def __eq__(self, other_conf):
        return self.clock == other_conf.clock


if __name__ == "__main__":
    ### PAS A JOUR !!!
    ### main COMPLETEMENT A REVOIR.
    p1 = Piece("1->0")
    p2 = Piece("0->1")
    soup = SoupSpec([OBCConfig(0)], [p1, p2])
    soup_sem = SoupSemantics(soup)
    s = Sem2RG(soup_sem)


# À faire : On a """fait""" une SoupConfiguration de OneBitClock, il faut en faire une pour AliceEtBob et Hanoi.

# Notes prises le 19/01/2024 :
#                                 predicate-|.
# Soup->SoupSemantic->Sem2RG->ParentTracer->bfs->getTrace
#                                  |--------|^
#
# Il nous manque un langage de propriétés qui nous permet de tester toutes les fonctions calculables.
# Pour faire le lien entre la SoupSemantic et la Semantic2RG.
# Il nous faudra aussi un produit synchrone entre la SoupSemantic et le langage qu'on va créer.
#       Il calculera l'intersection d'un modèle et la négation d'une propriété à tester.
# Enfin, il nous manque un Det Cycle : un truc par-dessus le bfs pour détecter les mauvaises boucles d'exécution.


# Notes du 26/01/24
# Il nous manque :
# 1) un Langage de propriétés, qui va :
#   taguer des cycles, tel un automate de Büchi, qui n'accepte que des mots qui contiennent un suffixe pouvant de
#   répéter indéfiniment.
#   La fonction d'historique, de comptage (ex. compter le nombre de fois ou Alice rentre en section critique).
#       On ne veut pas être obligés de mettre ce compteur dans le programme A&B à tester.
#       On ne chercherait qu'un seul cycle.
# 2) Une composition entre Soup et Lang_de_Prop.
# 3) Un algorithme de détection de cycles annotés (Tagged Cycles)
#
# La sémantique opérationnelle d'un automate : c'est le fait de parcourir l'automate et obtenir un mot : l'ensemble
# des mots qu'on peut générer en parcourant le DFA.
# La syntaxe, c'est l'automate lui-même, qui encore sa sémantique pourvue qu'on applique ses règles de parcours...


# Evaluation : S'axer sur la fonctionnalité.
#   Est-ce que les 3 implémentations d'A&B (ou les 2 arrivent en SC, ou il y a un deadlock, et ou tout marche bien, et
#   comment on a testé chacune des propriétés pour les 3 ?) ?
#       Les implémentations de Hanoi (littérales sur BFS, en SemToRG, et en Soup) ?


# Point 2) : Il y a dissymétrie entre le modèle (ex. A&B) et sa Soup. Pour résoudre ça, il faut une composition entre
# les deux.
# On introduit le concept de pas d'exécution (Step)
# Un pas d'exécution encode un état entrant, une action et un état sortant.
# Leur assemblage permet de reconstituer le parcourt du graphe et de voir l'évolution de variables au cours de la
# construction.
# La composition sera un opérateur entre le modèle et les propriétés.
# Voir classe StepSyncComposition dans synchronous_product.py.

# Point 3) : cf. dependent_semantics.

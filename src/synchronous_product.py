from semantics import Semantics
from soup_language import *
from dependent_semantics import *


class StepSyncComposition(Semantics):
    def __init__(self, lhs, rhs):
        self.lhs: SoupSemantics = lhs  # Left Hand Side, le modèle.
        self.rhs: DependentSoupSemantics = rhs  # Right Hand Side, la propriété à vérifier sur le modèle.

    # On implémente les 3 méthodes qui vont en faire une sémantique.
    def initial(self):
        initials = []
        for lhs_c in self.lhs.initial():  # c = configuration
            for rhs_c in self.rhs.initial():
                couple = (lhs_c, rhs_c)
                initials.append(couple)
        return initials

    def actions(self, source):  # source est un couple, comme ceux renvoyés par self.initial().
        # Donc, source est un couple de configurations.
        lhs_source, rhs_source = source
        sync_actions = []
        lhs_actions: list[Piece] = self.lhs.actions(lhs_source)  # ajout de .lhs. pour éviter de boucler
        # indéfiniment sur les self.actions.
        lhs_action_count = len(lhs_actions)  # Le code sera un peu tordu : le dernier état atteint ne sera jamais
        # considéré comme une source, mais on pourrait vouloir le faire, donc on rajoute un pas fictif nommé "deadlock"
        # vers le même état.
        for lhs_action in lhs_actions:  # lhs.actions est une liste de Pieces.
            lhs_targets: list[SoupConfiguration] = self.lhs.execute(lhs_action, lhs_source)
            if len(lhs_targets) == 0:
                lhs_action_count -= 1  # S'il n'y a aucune cible pour cette action, je suis en impasse.
            for lhs_target in lhs_targets:
                # On crée une nouvelle Step.
                lhs_step: tuple[SoupConfiguration, Piece, SoupConfiguration] = (lhs_source, lhs_action, lhs_target)
                rhs_actions: list[Piece] = self.rhs.actions(lhs_step, rhs_source)  # Le couple (lhs_step, rhs_source) est le
                # contexte d'exécution/d'évaluation.
                actions = map(lambda rhs_action: (lhs_step, rhs_action), rhs_actions)
                # type(actions) = list[tuple[SoupConfiguration, Piece, SoupConfiguration], Piece]
                sync_actions.extend(actions)
            if lhs_action_count == 0:  # Si action_count atteint 0, c'est que la configuration lhs_source est bien
                # un deadlock.
                lhs_step = (lhs_source, "deadlock", rhs_source)
                rhs_actions = self.rhs.actions(lhs_step, lhs_source)
                sync_actions.extend(map(lambda rhs_action: (lhs_step, rhs_action), rhs_actions))
        return sync_actions

    def execute(self, action, source: tuple[SoupConfiguration, SoupConfiguration]):
        # type(action) = list[tuple[SoupConfiguration, Piece, SoupConfiguration], Piece]
        lhs_step, rhs_action = action
        lhs_source, rhs_source = source
        rhs_targets = self.rhs.execute(rhs_action, lhs_step, rhs_source)  # Le couple (lhs_step, rhs_source) est le
        # contexte d'exécution/d'évaluation.
        return map(lambda rhs_target: (lhs_step[2], rhs_target), rhs_targets)

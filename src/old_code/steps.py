from abc import ABC, abstractmethod
from copy import deepcopy

from graph.breadth_first_search import bfs
from semantics import Semantics
from soup import Piece, SoupSemantic


class StepSyncComposition(Semantics):
    def __init__(self, lhs, rhs) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        initials = []
        for lhs_c in self.lhs.initial():
            for rhs_c in self.rhs.initial():
                initials.append((lhs_c, rhs_c))
        return initials

    def actions(self, source):
        lhs_source, rhs_source = source
        syncActions = []
        lhs_actions = self.lhs.actions(lhs_source)
        lhs_action_count = len(lhs_actions)
        for lhs_action in lhs_actions:
            lhs_targets = self.lhs.execute(lhs_action, lhs_source)
            if len(lhs_targets) == 0:
                for lhs_target in lhs_targets:
                    lhs_step = (lhs_source, lhs_action, lhs_target)
                    rhs_actions = self.rhs.actions(lhs_step, rhs_source)
                    actions = map(lambda rA: (lhs_target, rA), rhs_actions)
                    syncActions.extend(actions)
            if lhs_action_count == 0:
                lhs_step = lhs_source, "deadlock", lhs_source
                rhs_actions = self.rhs.actions(lhs_step, rhs_source)
                syncActions.extend(map(lambda rA: (lhs_source, rA), rhs_actions))
        return syncActions

    def execute(self, action, source):
        lhs_step, rhs_action = action
        lhs_source, rhs_source = source
        rhs_targets = self.rhs.execute(rhs_action, lhs_step, rhs_source)
        return map(lambda rhs_target: (lhs_step[2], rhs_target), rhs_targets)


class DependentSemantics(ABC):
    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, input, configuration):
        pass

    @abstractmethod
    def execute(self, action, input, configuration):
        pass


class DependentSoupSemantics(DependentSemantics):
    def __init__(self, soup: SoupSemantic) -> None:
        self.soup = soup

    def initial(self):
        return self.soup.initial()

    def actions(self, input, configuration):
        return filter(lambda p: p.guard(input, configuration), self.soup.pieces)

    def execute(self, action, input, configuration):
        src = deepcopy(configuration)
        inp = deepcopy(input)
        return action(inp, src)


if __name__ == "__main__":
    p1 = Piece("True", lambda i, c: c == i, lambda i, c: c)
    p2 = Piece("both in C", lambda i, c: c == 1, lambda i, c: c)

    bfs("...", lambda c: c[1] == 2)

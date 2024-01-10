from typing import List


class SoupConfiguration:
    def __hash__(self) -> int:
        pass

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, SoupConfiguration):
            return self.__hash__() == __value.__hash__()
        return NotImplemented

    def __repr__(self) -> str:
        pass


class Piece:
    def __init__(self, name: str):
        self.name: str = name
        self.guard = lambda c: c.clock == 1
        self.action = lambda c: None

    def enabled(self, config: SoupConfiguration):
        return self.guard(config)

    def execute(self, config: SoupConfiguration):
        return self.action(config)


class SoupSpec:
    def __init__(self, initialConfigs: List[SoupConfiguration], pieces:List[Piece]):
        self.configs = initialConfigs
        self.pieces = pieces

    def enabledPieces(self, config: SoupConfiguration) -> List[Piece]:
        return list(filter(lambda p: p.enabled(config), self.pieces))


class SoupSemantics:
    def __init__(self, spec: SoupSpec):
        self.spec = spec

    def initial(self):
        self.spec.initial()

    def actions(self, config: SoupConfiguration):
        self.spec.enabledPieces(config)

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
    s = Sem2RG(soup_sem)


# A faire : On a """fait""" une soupconfig de OneBitClock, il faut en faire une pour AliceetBob et Hanoi.
from typing import List


class SoupConfiguration:
    def __hash__(self) -> int:
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def __repr__(self) -> str:
        pass


class Piece:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.guard = lambda c: c.clock == 1
        self.action = lambda c: None

    def enabled(self, config: SoupConfiguration) -> bool:
        return self.guard(config)


class SoupSpec:
    def initial(self) -> List[SoupConfiguration]:
        return []

    def pieces(self) -> List[Piece]:
        return []

    def enabledPieces(self, config: SoupConfiguration) -> List[Piece]:
        return list(filter(lambda p: p.enabled(config), self.pieces()))

from src.semantics import Semantics


class Soup:
    def __init__(self):
        pass


class SoupSemantic(Semantics):
    def initial(self):
        # TODO: implement this
        return NotImplementedError

    def actions(self, configuration):
        pieces = (
            configuration.pieces
        )  # TODO: A verifier => récup les pieces à tout prix !
        for piece in pieces:
            if piece.cond(configuration):
                return piece.lbda(configuration)


class Piece:
    def __init__(self) -> None:
        self.cond = "soemthing"
        self.lbda = "lambda syntax"
        # TODO: implement this

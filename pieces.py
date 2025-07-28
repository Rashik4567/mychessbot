from typing import Literal, Self

from custom_exceptions import InvalidPieceError

_Types = Literal["K", "N", "Q", "R", "B", "P"]
_PositionsX = Literal[1, 2, 3, 4, 5, 6, 7, 8]
_PositionsY = Literal[1, 2, 3, 4, 5, 6, 7, 8]


class ChessPiece:
    def __init__(self, piece_type:_Types = "P", position_x:_PositionsX = 1, position_y:_PositionsY = 1):

        self.type = piece_type
        self.position = [position_x, position_y]

        if not self._validate():
            raise InvalidPieceError(self.validation_message)


    def _validate(self) -> bool:
        # TODO: Implement validation method for chess piece creation.
        self.validation_message = ""
        return True

    def legal_moves(self) -> list:
        # TODO: Implement method to return a list of all the available moves.
        return []

    def move(self, position:str) -> bool:
        return True

    def capture(self, piece:Self) -> bool:
        return True


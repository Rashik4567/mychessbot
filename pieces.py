from typing import Literal, Self

from custom_exceptions import InvalidPieceError

_Types = Literal["K", "N", "Q", "R", "B", "P"]
_PositionsX = Literal[1, 2, 3, 4, 5, 6, 7, 8]
_PositionsY = Literal[1, 2, 3, 4, 5, 6, 7, 8]


class ChessPiece:
    def __init__(self, piece_type:_Types, position_x:_PositionsX, position_y:_PositionsY, isWhite=True):

        self.piece_type:str = piece_type
        self.position_x:int = position_x
        self.position_y:int = position_y
        self.isWhite:bool = isWhite

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
        self.position_x = ord(position[0].lower()) - 96
        self.position_y = int(position[1])
        return True

    def capture(self, piece:Self) -> bool:
        return True


    def __repr__(self) -> str:
        if self.piece_type == "P":
            return f"{chr(96+self.position_x)}{self.position_y}"
        else:
            return f"{self.piece_type.lower()}{chr(96+self.position_x)}{self.position_y}"

class InvalidPieceError(Exception):
    """Piece is invalid.

    Probably because of invalid arguments for a ChessPiece
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IllegalMoveError(Exception):
    """Invalid move"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
from pieces import ChessPiece
from typing import Literal

_Notations = Literal["algebric", "fen"]


class Game:
    def __init__(self, notation:_Notations="algebric"):
        self.notation = notation
        self.board = []

        self.empty_squares:set[str] = set(())

        self.current_turn_for_white = True

        self.valid_moves_by_piece:dict[ChessPiece, list] = {}

        self.load_starting_position()
        self.valid_moves = self.get_all_valid_moves()

        print("List of valid moves:")
        print(self.valid_moves)


    def list_of_pieces_able_to_move(self, position:str) -> list:
        list_of_pieces:list[ChessPiece] = []

        for piece,all_moves in self.valid_moves_by_piece.items():
            if position in all_moves:
                list_of_pieces.append(piece)

        return list_of_pieces

    def algebric_notation(self, piece:ChessPiece, position_x:int, position_y:int) -> str:
        if piece.piece_type == "P":
            return f"{chr(96+position_x)}{position_y}"
        return f"{piece.piece_type}{chr(96+position_x)}{position_y}"

    def square_algebric_notation(self, position_x:int, position_y:int) -> str:
        return f"{chr(96+position_x)}{position_y}"



    def next_move(self, move:str):
        if not len(self.list_of_pieces_able_to_move(move)) == 1:
            print("Disambiguating move, please provide legal notation.")
            return
        if len(move) == 2:
            print("Pawn move")

            piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]


            self.empty_squares.remove(move)
            self.empty_squares.add(self.square_algebric_notation(piece_to_move.position_x, piece_to_move.position_y))
            piece_to_move.move(move)
        else:
            if (move[0].lower() == 'n'):
                print("Knight move")
                piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]
                self.empty_squares.remove(move[1:])
                self.empty_squares.add(self.square_algebric_notation(piece_to_move.position_x, piece_to_move.position_y))
                piece_to_move.move(move[1:])

            if (move[0].lower() == 'r'):
                print("Rook move")
                piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]
                self.empty_squares.remove(move[1:])
                self.empty_squares.add(self.square_algebric_notation(piece_to_move.position_x, piece_to_move.position_y))
                piece_to_move.move(move[1:])
            if (move[0].lower() == 'b'):
                print("Bishop move")
                piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]
                self.empty_squares.remove(move[1:])
                self.empty_squares.add(self.square_algebric_notation(piece_to_move.position_x, piece_to_move.position_y))
                piece_to_move.move(move[1:])


        self.current_turn_for_white = not self.current_turn_for_white
        self.valid_moves = self.get_all_valid_moves()
        print(f"Current board (turn for {'white' if self.current_turn_for_white else 'black'}): ")
        print(self.board)
        print("List of valid moves:")
        print(self.valid_moves)
        self.valid_moves = self.get_all_valid_moves()


    def get_all_valid_pawn_moves(self, piece:ChessPiece, isWhite:bool):
        valid_moves = []
        if isWhite:
            if piece.position_y == 2:
                if (self.algebric_notation(piece, piece.position_x, piece.position_y+1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y+1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y+1))
                if (self.algebric_notation(piece, piece.position_x, piece.position_y+2)) in self.empty_squares and (self.algebric_notation(piece, piece.position_x, piece.position_y+1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y+2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y+2))
            else:
                if (self.algebric_notation(piece, piece.position_x, piece.position_y+1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y+1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y+1))
        else:
            if piece.position_y == 7:
                if (self.algebric_notation(piece, piece.position_x, piece.position_y-1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y-1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y-1))
                if (self.algebric_notation(piece, piece.position_x, piece.position_y-2)) in self.empty_squares and (self.algebric_notation(piece, piece.position_x, piece.position_y-1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y-2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y-2))
            else:
                if (self.algebric_notation(piece, piece.position_x, piece.position_y-1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x, piece.position_y-1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, piece.position_y-1))
        return valid_moves


    def get_all_valid_knight_moves(self, piece:ChessPiece):
        valid_moves = []
        for i in range(2):
            if i%2 == 1:
                if (self.square_algebric_notation(piece.position_x+1, piece.position_y+2)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x+1, piece.position_y+2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+1, piece.position_y+2))
                if (self.square_algebric_notation(piece.position_x-1, piece.position_y-2)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x-1, piece.position_y-2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-1, piece.position_y-2))
                if (self.square_algebric_notation(piece.position_x+1, piece.position_y-2)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x+1, piece.position_y-2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+1, piece.position_y-2))
                if (self.square_algebric_notation(piece.position_x-1, piece.position_y+2)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x-1, piece.position_y+2))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-1, piece.position_y+2))
            else:
                if (self.square_algebric_notation(piece.position_x+2, piece.position_y+1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x+2, piece.position_y+1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+2, piece.position_y+1))
                if (self.square_algebric_notation(piece.position_x-2, piece.position_y-1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x-2, piece.position_y-1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-2, piece.position_y-1))
                if (self.square_algebric_notation(piece.position_x+2, piece.position_y-1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x+2, piece.position_y-1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+2, piece.position_y-1))
                if (self.square_algebric_notation(piece.position_x-2, piece.position_y+1)) in self.empty_squares:
                    valid_moves.append(self.algebric_notation(piece, piece.position_x-2, piece.position_y+1))
                    self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-2, piece.position_y+1))
        return valid_moves


    def get_all_valid_rook_moves(self, piece:ChessPiece):
        valid_moves = []

        for i in range(piece.position_x+1, 9, +1):
            if (self.square_algebric_notation(i, piece.position_y)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, i, piece.position_y))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, i, piece.position_y))
            else:
                break
        for i in range(piece.position_x-1, 0, -1):
            if (self.square_algebric_notation(i, piece.position_y)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, i, piece.position_y))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, i, piece.position_y))
            else:
                break
        for i in range(piece.position_y+1, 9, +1):
            if (self.square_algebric_notation(piece.position_x, i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x, i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, i))
            else:
                break
        for i in range(piece.position_y-1, 0, -1):
            if (self.square_algebric_notation(piece.position_x, i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x, i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x, i))
            else:
                break

        return valid_moves





    def get_all_valid_bishop_moves(self, piece:ChessPiece):
        valid_moves = []


        for i in range(8):
            if (self.square_algebric_notation(piece.position_x+i, piece.position_y+i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x+i, piece.position_y+i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+i, piece.position_y+i))
            else:
                break
        for i in range(8):
            if (self.square_algebric_notation(piece.position_x+i, piece.position_y-i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x+i, piece.position_y-i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x+i, piece.position_y-i))
            else:
                break

        for i in range(8):
            if (self.square_algebric_notation(piece.position_x-i, piece.position_y+i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x-i, piece.position_y+i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-i, piece.position_y+i))
            else:
                break
        for i in range(8):
            if (self.square_algebric_notation(piece.position_x-i, piece.position_y-i)) in self.empty_squares:
                valid_moves.append(self.algebric_notation(piece, piece.position_x-i, piece.position_y-i))
                self.valid_moves_by_piece[piece].append(self.algebric_notation(piece, piece.position_x-i, piece.position_y-i))
            else:
                break

        return valid_moves






    def get_all_valid_moves(self):
        valid_moves = []

        # Check moves of pawns and adds to valid moves if the move square is empty.
        if self.current_turn_for_white:
            for piece in self.board:
                if not (piece.isWhite):
                    continue
                self.valid_moves_by_piece[piece] = []

                if piece.piece_type == "P":
                    for move in self.get_all_valid_pawn_moves(piece, isWhite=True):
                        valid_moves.append(move)

                if piece.piece_type == "N":
                    for move in self.get_all_valid_knight_moves(piece):
                        valid_moves.append(move)

                if piece.piece_type == "R":
                    for move in self.get_all_valid_rook_moves(piece):
                        valid_moves.append(move)

                if piece.piece_type == "B":
                    for move in self.get_all_valid_bishop_moves(piece):
                        valid_moves.append(move)



        else:
            for piece in self.board:
                if (piece.isWhite):
                    continue
                self.valid_moves_by_piece[piece] = []

                if piece.piece_type == "P":
                    for move in self.get_all_valid_pawn_moves(piece, isWhite=False):
                        valid_moves.append(move)

                if piece.piece_type == "N":
                        for move in self.get_all_valid_knight_moves(piece):
                            valid_moves.append(move)

                if piece.piece_type == "R":
                    for move in self.get_all_valid_rook_moves(piece):
                        valid_moves.append(move)

                if piece.piece_type == "B":
                    for move in self.get_all_valid_bishop_moves(piece):
                        valid_moves.append(move)


        return valid_moves


    def is_finished(self):
        return False


    def load_starting_position(self) -> bool:
        """Loads the starting position in self.board list. returns True after loading successfully."""
        # white pawns
        self.board.append(ChessPiece(piece_type="P", position_x=1, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=2, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=3, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=4, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=5, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=6, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=7, position_y=2, isWhite=True))
        self.board.append(ChessPiece(piece_type="P", position_x=8, position_y=2, isWhite=True))


        # white back row pieces
        self.board.append(ChessPiece(piece_type="K", position_x=5, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="Q", position_x=4, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="R", position_x=1, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="R", position_x=8, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="N", position_x=2, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="N", position_x=7, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="B", position_x=3, position_y=1, isWhite=True))
        self.board.append(ChessPiece(piece_type="B", position_x=6, position_y=1, isWhite=True))

         # black pawns
        self.board.append(ChessPiece(piece_type="P", position_x=1, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=2, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=3, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=4, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=5, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=6, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=7, position_y=7, isWhite=False))
        self.board.append(ChessPiece(piece_type="P", position_x=8, position_y=7, isWhite=False))

         # black back row pieces
        self.board.append(ChessPiece(piece_type="K", position_x=5, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="Q", position_x=4, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="R", position_x=1, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="R", position_x=8, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="N", position_x=2, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="N", position_x=7, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="B", position_x=3, position_y=8, isWhite=False))
        self.board.append(ChessPiece(piece_type="B", position_x=6, position_y=8, isWhite=False))




        # Load empty squares to a list
        self.empty_squares.add("a3")
        self.empty_squares.add("b3")
        self.empty_squares.add("c3")
        self.empty_squares.add("d3")
        self.empty_squares.add("e3")
        self.empty_squares.add("f3")
        self.empty_squares.add("g3")
        self.empty_squares.add("h3")
        self.empty_squares.add("a4")
        self.empty_squares.add("b4")
        self.empty_squares.add("c4")
        self.empty_squares.add("d4")
        self.empty_squares.add("e4")
        self.empty_squares.add("f4")
        self.empty_squares.add("g4")
        self.empty_squares.add("h4")
        self.empty_squares.add("a5")
        self.empty_squares.add("b5")
        self.empty_squares.add("c5")
        self.empty_squares.add("d5")
        self.empty_squares.add("e5")
        self.empty_squares.add("f5")
        self.empty_squares.add("g5")
        self.empty_squares.add("h5")
        self.empty_squares.add("a6")
        self.empty_squares.add("b6")
        self.empty_squares.add("c6")
        self.empty_squares.add("d6")
        self.empty_squares.add("e6")
        self.empty_squares.add("f6")
        self.empty_squares.add("g6")
        self.empty_squares.add("h6")

        return True

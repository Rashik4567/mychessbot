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



    def next_move(self, move:str):
        if not len(self.list_of_pieces_able_to_move(move)) == 1:
            print("Disambiguating move, please provide legal notation.")
            return
        if len(move) == 2:
            print("Pawn move")

            piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]


            self.empty_squares.remove(move)
            self.empty_squares.add(f"{chr(96+piece_to_move.position_x)}{piece_to_move.position_y}")
            piece_to_move.move(move)
        else:
            if (move[0].lower() == 'n'):
                print("Knight move")
                piece_to_move:ChessPiece = self.list_of_pieces_able_to_move(move)[0]
                self.empty_squares.remove(move[1:])
                self.empty_squares.add(f"{chr(96+piece_to_move.position_x)}{piece_to_move.position_y}")
                piece_to_move.move(move[1:])
        self.current_turn_for_white = not self.current_turn_for_white
        self.valid_moves = self.get_all_valid_moves()
        print(f"Current board (turn for {'white' if self.current_turn_for_white else 'black'}): ")
        print(self.board)
        print("List of valid moves:")
        print(self.valid_moves)
        self.valid_moves = self.get_all_valid_moves()





    def get_all_valid_moves(self):
        valid_moves = []

        # Check moves of pawns and adds to valid moves if the move square is empty.
        if self.current_turn_for_white:
            for piece in self.board:
                if not (piece.isWhite):
                    continue
                self.valid_moves_by_piece[piece] = []
                if piece.piece_type == "P":
                    if piece.position_y == 2:
                        if (f"{chr(96+piece.position_x)}{piece.position_y+1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+1}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y+1}")
                        if (f"{chr(96+piece.position_x)}{piece.position_y+2}") in self.empty_squares and (f"{chr(96+piece.position_x)}{piece.position_y+1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+2}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y+2}")
                    else:
                        if (f"{chr(96+piece.position_x)}{piece.position_y+1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+1}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y+1}")

                if piece.piece_type == "N":
                    for i in range(2):
                        if i%2 == 1:
                            if (f"{chr(96+piece.position_x+1)}{piece.position_y+2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+1)}{piece.position_y+2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+1)}{piece.position_y+2}")
                            if (f"{chr(96+piece.position_x-1)}{piece.position_y-2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-1)}{piece.position_y-2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-1)}{piece.position_y-2}")
                            if (f"{chr(96+piece.position_x+1)}{piece.position_y-2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+1)}{piece.position_y-2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+1)}{piece.position_y-2}")
                            if (f"{chr(96+piece.position_x-1)}{piece.position_y+2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-1)}{piece.position_y+2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-1)}{piece.position_y+2}")
                        else:
                            if (f"{chr(96+piece.position_x+2)}{piece.position_y+1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+2)}{piece.position_y+1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+2)}{piece.position_y+1}")
                            if (f"{chr(96+piece.position_x-2)}{piece.position_y-1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-2)}{piece.position_y-1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-2)}{piece.position_y-1}")
                            if (f"{chr(96+piece.position_x+2)}{piece.position_y-1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+2)}{piece.position_y-1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+2)}{piece.position_y-1}")
                            if (f"{chr(96+piece.position_x-2)}{piece.position_y+1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-2)}{piece.position_y+1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-2)}{piece.position_y+1}")



        else:
            for piece in self.board:
                if (piece.isWhite):
                    continue
                self.valid_moves_by_piece[piece] = []
                if piece.piece_type == "P":
                    if piece.position_y == 7:
                        if (f"{chr(96+piece.position_x)}{piece.position_y-1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-1}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y-1}")
                        if (f"{chr(96+piece.position_x)}{piece.position_y-2}") in self.empty_squares and (f"{chr(96+piece.position_x)}{piece.position_y-1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-2}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y-2}")
                    else:
                        if (f"{chr(96+piece.position_x)}{piece.position_y-1}") in self.empty_squares:
                            valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-1}")
                            self.valid_moves_by_piece[piece].append(f"{chr(96+piece.position_x)}{piece.position_y-1}")


                if piece.piece_type == "N":
                    for i in range(2):
                        if i%2 == 1:
                            if (f"{chr(96+piece.position_x+1)}{piece.position_y+2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+1)}{piece.position_y+2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+1)}{piece.position_y+2}")
                            if (f"{chr(96+piece.position_x-1)}{piece.position_y-2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-1)}{piece.position_y-2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-1)}{piece.position_y-2}")
                            if (f"{chr(96+piece.position_x+1)}{piece.position_y-2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+1)}{piece.position_y-2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+1)}{piece.position_y-2}")
                            if (f"{chr(96+piece.position_x-1)}{piece.position_y+2}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-1)}{piece.position_y+2}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-1)}{piece.position_y+2}")
                        else:
                            if (f"{chr(96+piece.position_x+2)}{piece.position_y+1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+2)}{piece.position_y+1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+2)}{piece.position_y+1}")
                            if (f"{chr(96+piece.position_x-2)}{piece.position_y-1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-2)}{piece.position_y-1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-2)}{piece.position_y-1}")
                            if (f"{chr(96+piece.position_x+2)}{piece.position_y-1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x+2)}{piece.position_y-1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x+2)}{piece.position_y-1}")
                            if (f"{chr(96+piece.position_x-2)}{piece.position_y+1}") in self.empty_squares:
                                valid_moves.append(f"N{chr(96+piece.position_x-2)}{piece.position_y+1}")
                                self.valid_moves_by_piece[piece].append(f"N{chr(96+piece.position_x-2)}{piece.position_y+1}")

        return valid_moves

    # def get_valid_moves_per_piece(self, piece:ChessPiece):
    #     valid_moves = []

    #     # Check moves of pawns and adds to valid moves if the move square is empty.
    #     if self.current_turn_for_white:
    #         if piece.piece_type == "P" and piece.isWhite:
    #             if piece.position_y == 2:
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y+1}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+1}")
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y+2}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+2}")
    #             else:
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y+1}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y+1}")
    #         else:
    #             return valid_moves
    #     else:
    #         if piece.piece_type == "P" and not piece.isWhite:
    #             if piece.position_y == 7:
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y-1}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-1}")
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y-2}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-2}")
    #             else:
    #                 if (f"{chr(96+piece.position_x)}{piece.position_y-1}") in self.empty_squares:
    #                     valid_moves.append(f"{chr(96+piece.position_x)}{piece.position_y-1}")
    #         else:
    #             return valid_moves

    #     return valid_moves


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

from .board import (Board, PositionError)
from .knight import Knight
from .queen import Queen
from .rook import Rook


class PieceNotFoundError(Exception): pass


def create_piece(piece):
    """Factory function to create pieces.

    Input: piece, a string like "queen"

    Output: an instance of a subclass of Piece

    Raises exception if the string "piece" is not a known piece.

    """

    piece_map = {
        'rook': Rook,
        'knight': Knight,
        'queen': Queen,
    }

    if piece not in piece_map:
        raise PieceNotFoundError()

    return piece_map[piece]()

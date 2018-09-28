from .board import (Board, PositionError)
from .knight import Knight
from .queen import Queen
from .rook import Rook

piece_map = {
    'rook': Rook,
    'knight': Knight,
    'queen': Queen,
}

class PieceNotFoundError(Exception): pass


def create_piece(piece):
    """Factory function to create pieces."""
    if piece not in piece_map:
        raise PieceNotFoundError()
    return piece_map[piece]()

from .piece import Piece

class Rook(Piece):
    name = 'Rook'

    def moves_algorithm(self, coordinates):
        return self._determine_horizontal_and_vertical_moves(coordinates)

from .piece import Piece

class Rook(Piece):
    name = 'Rook'

    def moves_algorithm(self, coordinates):
        moves_coordinates = list()
        (row, col) = coordinates
        horizontal = [(r, col) for r in range(8) if r != row]
        vertical = [(row, c) for c in range(8) if c != col]
        return horizontal + vertical

from .piece import Piece
from .board import BOARD_MIN, BOARD_MAX

class Knight(Piece):
    name = 'Knight'

    def __init__(self):
        """Set up a list of move parameters.

        Do this once when instantiated, since we'll need it over the
        life of the piece.

        """
        self.move_params = list()

        for x in (2, -2):
            for y in (1, -1):
                self.move_params.append((x, y))
                self.move_params.append((y, x))


    def moves_algorithm(self, coordinates):
        moves_coordinates = list()
        for move in self.move_params:
            row = coordinates[0] + move[0]
            col = coordinates[1] + move[1]
            if row < BOARD_MIN or col < BOARD_MIN:
                continue
            if row > BOARD_MAX or col > BOARD_MAX:
                continue
            moves_coordinates.append((row, col))
        return moves_coordinates

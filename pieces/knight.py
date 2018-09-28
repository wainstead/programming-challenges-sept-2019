from .piece import Piece

class Knight(Piece):
    name = 'Knight'
    moves = list()

    def __init__(self):
        for x in (2, -2):
            for y in (1, -1):
                self.moves.append((x, y))
                self.moves.append((y, x))

    def moves_algorithm(self, coordinates):
        moves_coordinates = list()
        for move in self.moves:
            x = coordinates[0] + move[0]
            y = coordinates[1] + move[1]
            if x < 0 or y < 0:
                continue
            if x > 7 or y > 7:
                continue
            moves_coordinates.append((x, y))
        return moves_coordinates

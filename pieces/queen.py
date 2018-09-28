from .piece import Piece

class Queen(Piece):
    name = 'Queen'


    def moves_algorithm(self, coordinates):
        (row, col) = coordinates

        # Shamelessly borrowed from the rook. Share!
        horizontal = [(r, col) for r in range(8) if r != row]
        vertical = [(row, c) for c in range(8) if c != col]

        moves_coordinates = horizontal + vertical

        directions = (
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        )

        for direction in ,directions:
            on_the_board = True
            (x, y) = (row, col) # Start from the current position
            while on_the_board:
                (x, y) = (x + direction[0], y + direction[1])
                if (x not in range(8)) or (y not in range(8)):
                    on_the_board = False
                else:
                    moves_coordinates.append((x, y))

        return moves_coordinates

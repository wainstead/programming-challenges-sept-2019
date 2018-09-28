from .piece import Piece

class Queen(Piece):
    name = 'Queen'


    def moves_algorithm(self, coordinates):
        moves_coordinates = self._determine_horizontal_and_vertical_moves(coordinates)
        (row, col) = coordinates

        directions = (
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        )

        for direction in directions:
            on_the_board = True
            (x, y) = (row, col) # Start from the current position
            while on_the_board:
                (x, y) = (x + direction[0], y + direction[1])
                if (x not in range(8)) or (y not in range(8)):
                    on_the_board = False
                else:
                    moves_coordinates.append((x, y))

        return moves_coordinates

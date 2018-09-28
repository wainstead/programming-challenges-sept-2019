class Piece(object):

    def moves_algorithm(self):
        raise Exception("Subclasses must implement")

    def _determine_horizontal_and_vertical_moves(self, coordinates):
        """Common code for the rook and queen.

        Both pieces move horizontally and vertically.

        Returns a list of tuples; each tuple will be a board coordinate.

        """

        (row, col) = coordinates
        horizontal = [(r, col) for r in range(8) if r != row]
        vertical = [(row, c) for c in range(8) if c != col]
        return horizontal + vertical


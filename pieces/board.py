BOARD_MIN = 0
BOARD_MAX = 7


class PositionError(Exception): pass

class Board(object):
    """Implements a chess board.

    Internally we represent the board as a list of lists: a list of
    length eight, representing the board rows from top to bottom, and
    each row having a list of length eight representing the column
    positions. This makes the math of calculating moves easier to
    reason about.

    """

    # For fast lookup of positions (is 'a9' a square?)
    # and for fast lookup of a piece's position
    squares = dict()

    def __init__(self):
        # initialize our chessboard
        col_letters = 'abcdefgh'
        row_numbers = list(range(1,9))
        self.chessboard = list(range(8))

        for row in range(8):
            row_num = row_numbers.pop()
            #print("setting row %s to new list" % row)
            self.chessboard[row] = list(range(8))
            for col in range(8):
                #print("setting %s %s" % (row_num, col_letters[col]))
                position = "{}{}".format(col_letters[col], row_num)
                self.chessboard[row][col] = position
                self.squares[position] = [(row, col), None]

    def clear_board(self):
        for position in self.squares:
            self.squares[position][1] = None

    def place_piece(self, piece, position):
        if not position in self.squares:
            raise PositionError()
        self.squares[position][1] = piece

    def _get_piece_position(self, piece):
        for position in self.squares:
            if self.squares[position][1] == piece:
                return self.squares[position][0]

    def list_possible_moves(self, piece):
        piece_coordinates = self._get_piece_position(piece)
        moves_coordinates = piece.moves_algorithm(piece_coordinates)
        possible_moves = list()
        for (row, col) in moves_coordinates:
            try:
                possible_moves.append(self.chessboard[row][col])
            except IndexError:
                pass

        possible_moves.sort()
        return possible_moves

    def __repr__(self):
        board_as_str = ""
        for row in range(8):
            for col in range(8):
                board_as_str += "({}, {}: {}) ".format(
                    row, col, self.chessboard[row][col])
            board_as_str += "\n"
        for position in self.squares:
            if self.squares[position][1]:
                board_as_str += "{}: {}\n".format(
                    position, self.squares[position][1].name)
        return board_as_str

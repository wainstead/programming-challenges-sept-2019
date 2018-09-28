class PositionError(Exception): pass

class Board(object):
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
                self.squares[position] = None

    def place_piece(self, piece, position):
        if not position in self.squares:
            raise PositionError()
        self.squares[position] = piece

    def __repr__(self):
        board_as_str = ""
        for row in range(8):
            for col in range(8):
                board_as_str += "{}, {}: {} ".format(
                    row, col, self.chessboard[row][col])
            board_as_str += "\n"
        return board_as_str

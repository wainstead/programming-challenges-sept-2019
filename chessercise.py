import argparse
from pieces import Board, create_piece, Knight, Queen, Rook


parser = argparse.ArgumentParser()
parser.add_argument('-piece', dest='piece', required=True,
                    help='The piece to move')
parser.add_argument('-position', dest='position', required=True,
                    help='The starting position of the piece')

args = parser.parse_args()

position = args.position.lower()

print("{} and {}".format(piece, position))

piece = create_piece(args.piece.lower())
assert type(piece) in (Knight, Queen, Rook)
board = Board()

# board.place_piece(piece, position)
# board.get_moves(piece)
# Algorithms.

# unittest. The code has to be testable.

# Implement bishop as well as rook, and you have the queen.


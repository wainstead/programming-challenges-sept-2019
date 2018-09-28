import argparse
from pieces import Board, create_piece

parser = argparse.ArgumentParser()
parser.add_argument('-piece', dest='piece', required=True,
                    help='The piece to move')
parser.add_argument('-position', dest='position', required=True,
                    help='The starting position of the piece')
args = parser.parse_args()

position = args.position.lower()
# Instantiate the piece's class from user input
piece = create_piece(args.piece.lower())

board = Board()
# The board has-a piece
board.place_piece(piece, position)

# The board tells us the possible moves
possible_moves = board.list_possible_moves(piece)

print("Moves for {} at {}:".format(piece.name, position))
print(", ".join(possible_moves))

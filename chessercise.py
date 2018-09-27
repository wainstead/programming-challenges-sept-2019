from pieces import Rook

# User input.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-piece', dest='piece', required=True,
                    help='The piece to move')
parser.add_argument('-position', dest='position', required=True,
                    help='The starting position of the piece')

args = parser.parse_args()

assert args.piece and args.position

print("{} and {}".format(args.piece, args.position))


# Algorithms.

# unittest. The code has to be testable.

# Implement bishop as well as rook, and you have the queen.


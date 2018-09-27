import unittest
from pieces import Piece, Rook, Queen, Knight

class TestPiece(unittest.TestCase):

    def setUp(self):
        pass
    def testConstructors(self):
        p = Piece()
        r = Rook()
        q = Queen()
        k = Knight()

if __name__ == '__main__':
    unittest.main()

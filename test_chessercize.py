import unittest
from pieces import (
    create_piece, Board, Knight, Queen, Rook, PieceNotFoundError
)

class TestPieces(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructors(self):
        b = Board()
        r = Rook()
        q = Queen()
        k = Knight()

    def test_pieces_by_name(self):
        for piece in ('knight', 'queen', 'rook'):
            create_piece(piece)

    def test_bogus_piece(self):
        failed_correctly = False
        try:
            piece = create_piece('checker')
        except PieceNotFoundError:
            failed_correctly = True

        assert failed_correctly, "Created nonexistent piece!"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

import unittest
from pieces import ( create_piece, Board, Knight, Queen, Rook,
                     PieceNotFoundError, PositionError )

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

    def test_chessboard(self):
        b = Board()
        assert b.chessboard[0][0] == 'a8', b.chessboard[0][0]
        assert b.chessboard[7][7] == 'h1', b.chessboard[7][7]

    def test_placing_piece(self):
        r = Rook()
        b = Board()
        b.place_piece(r, 'd2')
        assert b.squares[b.chessboard[6][3]] == r

    def test_bad_position(self):
        r = Rook()
        b = Board()
        failed_correctly = False
        try:
            b.place_piece(r, 'x42')
        except PositionError:
            failed_correctly = True
        assert failed_correctly

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

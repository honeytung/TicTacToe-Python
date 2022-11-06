import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_make_empty_board(self):
        board = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]
        self.assertEqual(logic.make_empty_board(), board)

    def test_get_winner(self):
        board1 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X']
        ]
        board2 = [
            ['X', None, 'O'],
            [None, 'O', None],
            ['O', 'O', 'X']
        ]
        board3 = [
            ['X', 'X', 'X'],
            [None, 'X', None],
            [None, 'O', 'O']
        ]
        board4 = [
            ['X', None, 'O'],
            [None, 'O', 'O'],
            [None, 'O', 'O']
        ]
        board5 = [
            ['X', None, 'O'],
            [None, 'O', 'X'],
            [None, 'O', 'O']
        ]
        self.assertEqual(logic.get_winner(board1), 'X')
        self.assertEqual(logic.get_winner(board2), 'O')
        self.assertEqual(logic.get_winner(board3), 'X')
        self.assertEqual(logic.get_winner(board4), 'O')
        self.assertEqual(logic.get_winner(board5), None)

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

    def test_get_board_from_index(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X']
        ]
        self.assertEqual(logic.get_board_from_index(board, 1), 'X')
        self.assertEqual(logic.get_board_from_index(board, 6), None)
        self.assertEqual(logic.get_board_from_index(board, 8), 'O')

    def test_check_index(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X']
        ]
        self.assertEqual(logic.check_index(board, 1), False)
        self.assertEqual(logic.check_index(board, 6), True)
        self.assertEqual(logic.check_index(board, 8), False)


if __name__ == '__main__':
    unittest.main()

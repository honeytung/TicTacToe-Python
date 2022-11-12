import unittest
import logic


class TestBoard(unittest.TestCase):

    def test_initialize_board(self):
        board = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

        board_test = logic.Board()
        self.assertEqual(board, board_test.board)

    def test_clear_board(self):
        board = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

        board_test = logic.Board()
        board_test.board = [['1', '2', 'X'],
                            ['4', 'X', '6'],
                            ['7', 'O', 'O']]
        board_test.clear_board()

        self.assertEqual(board, board_test.board)

    def test_get_winner(self):
        board1 = [['X', '2', 'O'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'X']]
        board2 = [['X', '2', 'O'],
                  ['4', 'O', '6'],
                  ['O', 'O', 'X']]
        board3 = [['X', 'X', 'X'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'O']]
        board4 = [['X', '2', 'O'],
                  ['4', 'O', 'O'],
                  ['7', 'O', 'O']]
        board5 = [['X', '2', 'O'],
                  ['4', 'O', 'X'],
                  ['7', 'O', 'O']]
        board6 = [['O', 'X', 'O'],
                  ['O', 'X', 'X'],
                  ['X', 'O', 'O']]

        board_test = logic.Board()

        board_test.board = board1
        self.assertEqual('X', board_test.get_winner())
        board_test.board = board2
        self.assertEqual('O', board_test.get_winner())
        board_test.board = board3
        self.assertEqual('X', board_test.get_winner())
        board_test.board = board4
        self.assertEqual('O', board_test.get_winner())
        board_test.board = board5
        self.assertEqual(None, board_test.get_winner())
        board_test.board = board6
        self.assertEqual(None, board_test.get_winner())

    def test_get_character_from_index(self):
        board = [['X', '2', 'O'],
                 ['4', 'X', '6'],
                 ['7', 'O', 'X']]

        board_test = logic.Board()
        board_test.board = board

        self.assertEqual('X', board_test.get_character_from_index(1))
        self.assertEqual('6', board_test.get_character_from_index(6))
        self.assertEqual('O', board_test.get_character_from_index(8))

    def test_check_index(self):
        board = [['X', '2', 'O'],
                 ['4', 'X', '6'],
                 ['7', 'O', 'X']]

        board_test = logic.Board()
        board_test.board = board

        self.assertEqual(False, board_test.check_index(1))
        self.assertEqual(True, board_test.check_index(6))
        self.assertEqual(False, board_test.check_index(8))

    def test_update_board(self):
        board1 = [['X', '2', 'O'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'X']]
        board1_updated = [['X', 'O', 'O'],
                          ['4', 'X', '6'],
                          ['7', 'O', 'X']]
        board2 = [['X', '2', 'O'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'X']]
        board2_updated = [['X', '2', 'O'],
                          ['4', 'X', 'X'],
                          ['7', 'O', 'X']]

        board_test = logic.Board()

        board_test.board = board1
        board_test.update_board(2, 'O')
        self.assertEqual(board1_updated, board_test.board)
        board_test.board = board2
        board_test.update_board(6, 'X')
        self.assertEqual(board2_updated, board_test.board)
        board_test.board = board1
        board_test.update_board(3, 'O')
        self.assertEqual(board1, board_test.board)
        board_test.board = board2
        board_test.update_board(3, 'X')
        self.assertEqual(board2, board_test.board)

    def test_check_draw(self):
        board1 = [['X', '2', 'O'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'X']]
        board2 = [['X', '2', 'O'],
                  ['4', 'O', '6'],
                  ['O', 'O', 'X']]
        board3 = [['X', 'O', 'X'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'O']]
        board4 = [['X', '2', 'O'],
                  ['4', 'O', 'X'],
                  ['7', 'O', 'O']]
        board5 = [['X', 'X', 'O'],
                  ['O', 'O', 'X'],
                  ['X', 'O', 'O']]
        board6 = [['O', 'X', 'O'],
                  ['O', 'X', 'X'],
                  ['X', 'O', 'O']]

        board_test = logic.Board()

        board_test.board = board1
        self.assertEqual(False, board_test.check_draw())
        board_test.board = board2
        self.assertEqual(False, board_test.check_draw())
        board_test.board = board3
        self.assertEqual(False, board_test.check_draw())
        board_test.board = board4
        self.assertEqual(False, board_test.check_draw())
        board_test.board = board5
        self.assertEqual(True, board_test.check_draw())
        board_test.board = board6
        self.assertEqual(True, board_test.check_draw())


class TestHuman(unittest.TestCase):

    def test_initialize_human(self):
        player1 = 'O'
        player2 = 'X'

        test_player1 = logic.Human(player1)
        test_player2 = logic.Human(player2)

        self.assertEqual(player1, test_player1.player)
        self.assertEqual(player2, test_player2.player)

    def test_get_move(self):
        player1 = 'O'
        player2 = 'X'

        board1 = [['X', '2', 'O'],
                  ['4', 'X', 'X'],
                  ['7', 'O', 'O']]
        board1_updated = [['X', 'O', 'O'],
                          ['4', 'X', 'X'],
                          ['7', 'O', 'O']]
        board2 = [['X', '2', 'O'],
                  ['4', 'X', '6'],
                  ['7', 'O', 'O']]
        board2_updated = [['X', '2', 'O'],
                          ['4', 'X', 'X'],
                          ['7', 'O', 'O']]

        test_player1 = logic.Human(player1)
        test_player2 = logic.Human(player2)
        test_board1 = logic.Board()
        test_board2 = logic.Board()

        test_board1.board = board1
        test_board2.board = board2

        test_player1.get_move(test_board1, 3)
        self.assertEqual(board1, test_board1.board)
        test_player1.get_move(test_board1, 2)
        self.assertEqual(board1_updated, test_board1.board)
        test_player2.get_move(test_board2, 5)
        self.assertEqual(board2, test_board2.board)
        test_player2.get_move(test_board2, 6)
        self.assertEqual(board2_updated, test_board2.board)


if __name__ == '__main__':
    unittest.main()

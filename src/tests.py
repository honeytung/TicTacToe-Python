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
            ['X', '2', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        board2 = [
            ['X', '2', 'O'],
            ['4', 'O', '6'],
            ['O', 'O', 'X']]
        board3 = [
            ['X', 'X', 'X'],
            ['4', 'X', '6'],
            ['7', 'O', 'O']]
        board4 = [
            ['X', '2', 'O'],
            ['4', 'O', 'O'],
            ['7', 'O', 'O']]
        board5 = [
            ['X', '2', 'O'],
            ['4', 'O', 'X'],
            ['7', 'O', 'O']]
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
            ['X', '2', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        self.assertEqual(logic.get_board_from_index(board, 1), 'X')
        self.assertEqual(logic.get_board_from_index(board, 6), '6')
        self.assertEqual(logic.get_board_from_index(board, 8), 'O')

    def test_check_index(self):
        board = [
            ['X', '2', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        self.assertEqual(logic.check_index(board, 1), False)
        self.assertEqual(logic.check_index(board, 6), True)
        self.assertEqual(logic.check_index(board, 8), False)


    def test_update_board(self):
        board1 = [
            ['X', '2', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        board1_updated = [
            ['X', 'O', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        board2 = [
            ['X', '2', 'O'],
            ['4', 'X', '6'],
            ['7', 'O', 'X']]
        board2_updated = [
            ['X', '2', 'O'],
            ['4', 'X', 'X'],
            ['7', 'O', 'X']]
        self.assertEqual(logic.update_board(board1, 2, 'O'), board1_updated)
        self.assertEqual(logic.update_board(board2, 6, 'X'), board2_updated)
        self.assertEqual(logic.update_board(board1, 3, 'O'), board1)
        self.assertEqual(logic.update_board(board2, 3, 'X'), board2)


if __name__ == '__main__':
    unittest.main()

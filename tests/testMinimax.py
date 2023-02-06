import unittest
from minimax import minimax
from importTestBoards import readFile, END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD


class MyTestCase(unittest.TestCase):
    def test_endEasy(self):
        test_boards = readFile(END_EASY)
        self.do_for_boards(test_boards)
        print("End Easy Done")

    def do_for_boards(self, test_boards):
        for board, expected_score in test_boards:
            score = minimax(board)
            print("Expected: " + str(expected_score) + " Actual: " + str(score))
            self.assertEqual(expected_score, score)


if __name__ == '__main__':
    unittest.main()

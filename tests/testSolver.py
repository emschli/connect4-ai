import unittest
from importTestBoards import readFile, END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
from config import solver


class SolverAccuracyTest(unittest.TestCase):
    # methode muss test am anfang stehen haben
    def test_endEasy(self):
        test_boards = readFile(END_EASY)
        self.do_for_boards(test_boards)
        print(END_EASY + " done!")

    def test_middleEasy(self):
        test_boards = readFile(MIDDLE_EASY)
        self.do_for_boards(test_boards)
        print(MIDDLE_EASY + " done!")

    def test_middleMedium(self):
        test_boards = readFile(MIDDLE_MEDIUM)
        self.do_for_boards(test_boards)
        print(MIDDLE_MEDIUM + " done!")

    def test_beginEasy(self):
        test_boards = readFile(BEGIN_EASY)
        self.do_for_boards(test_boards)
        print(BEGIN_EASY + " done!")

    def test_beginMedium(self):
        test_boards = readFile(BEGIN_MEDIUM)
        self.do_for_boards(test_boards)
        print(BEGIN_MEDIUM + " done!")

    def test_beginHard(self):
        test_boards = readFile(BEGIN_HARD)
        self.do_for_boards(test_boards)
        print(BEGIN_HARD + " done!")

    def do_for_boards(self, test_boards):
        for board, expected_score in test_boards:
            score = solver.solve(board)
            print("Expected: " + str(expected_score) + " Actual: " + str(score))
            self.assertEqual(expected_score, score)


if __name__ == '__main__':
    unittest.main()

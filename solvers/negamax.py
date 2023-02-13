from math import inf as infinity
from Board import Board


class Negamax:
    version = '_v1'
    default_board = Board

    def __init__(self):
        self.positionCount = 0

    def getScore(self, board):
        return int((board.rows * board.columns - board.numberOfPiecesPlayed + 1) / 2)

    def _negamax(self, board):
        self.positionCount += 1
        if board.isFull():
            return 0

        for i in range(board.columns):
            if not board.columnIsFull(i) and board.wouldBeWin(i):
                return self.getScore(board)

        best_score = -infinity

        for i in range(board.columns):
            if not board.columnIsFull(i):
                column_index, row_index = board.insertPiece(i)

                score = -self._negamax(board)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                best_score = max(score, best_score)

        return best_score

    def solve(self, board):
        self.positionCount = 0
        return self._negamax(board)

    def getBestMove(self, board):
        best_score = -infinity
        chosen_column = None

        for i in range(board.columns):
            if not board.columnIsFull(i):
                column_index, row_index = board.insertPiece(i)

                score = -self.solve(board)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                if score > best_score:
                    chosen_column = column_index
                    best_score = score

        return chosen_column

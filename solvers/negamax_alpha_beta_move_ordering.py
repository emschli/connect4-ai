from math import inf as infinity
from Board import Board


class NegamaxAlphaBetaMoveOrdering:
    version = '_v3'
    default_board = Board

    def __init__(self):
        self.positionCount = 0
        self.explorationOrder = [3, 2, 4, 5, 1, 0, 6]

    def getScore(self, board):
        return int((board.rows * board.columns - board.numberOfPiecesPlayed + 1) / 2)

    def _negamax(self, board, alpha, beta):
        self.positionCount += 1
        if board.isFull():
            return 0

        for i in range(board.columns):
            if not board.columnIsFull(i) and board.wouldBeWin(i):
                return self.getScore(board)

        max_score = int((board.columns * board.rows - 1 - board.numberOfPiecesPlayed) / 2)
        if beta > max_score:
            beta = max_score
            if alpha >= beta:
                return beta

        for i in self.explorationOrder:
            if not board.columnIsFull(i):
                column_index, row_index = board.insertPiece(i)

                score = -self._negamax(board, -beta, -alpha)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                if score >= beta:
                    return score

                alpha = max(alpha, score)

        return alpha

    def solve(self, board):
        self.positionCount = 0
        return self._negamax(board, -infinity, infinity)

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

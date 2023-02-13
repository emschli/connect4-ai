from math import inf as infinity


class NegamaxAlphaBeta:
    version = '_v2'

    def __init__(self):
        self.positionCount = 0

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

        for i in range(board.columns):
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

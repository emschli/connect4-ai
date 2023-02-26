from math import inf as infinity
from BitBoard import BitBoard


class NegamaxWithBitboard:
    version = '_v4'
    default_board = BitBoard

    def __init__(self):
        self.positionCount = 0
        self.explorationOrder = [3, 2, 4, 5, 1, 0, 6]

    def getScore(self, board):
        return int((board.rows * board.columns - board.numberOfPiecesPlayed + 2) / 2)

    def _negamax(self, board, alpha, beta):
        self.positionCount += 1
        possible_moves = board.getPossibleMoves()

        if not possible_moves:
            return 0

        for i in possible_moves:
            board.insertPiece(i)
            if board.isWin():
                score = self.getScore(board)
                board.undoMove()
                return score
            board.undoMove()

        max_score = int((board.columns * board.rows - 1 - board.numberOfPiecesPlayed) / 2)
        if beta > max_score:
            beta = max_score
            if alpha >= beta:
                return beta

        for i in self.explorationOrder:
            if i in possible_moves:
                board.insertPiece(i)

                score = -self._negamax(board, -beta, -alpha)

                board.undoMove()

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

        for i in board.getPossibleMoves():
            board.insertPiece(i)

            if board.isWin():
                board.undoMove()
                return i

            score = -self.solve(board)

            board.undoMove()

            if score > best_score:
                chosen_column = i
                best_score = score

        return chosen_column

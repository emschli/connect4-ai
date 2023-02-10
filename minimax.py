from math import inf as infinity


class Minimax:
    version = '_v0'

    def __init__(self):
        self.positionCount = 0

    def getScore(self, board, isMaximizingPlayer):
        score = int((board.rows * board.columns - board.numberOfPiecesPlayed + 1) / 2)
        return score if isMaximizingPlayer else -score

    def minimax(self, board, isMaximizingPlayer):
        self.positionCount += 1
        if board.isFull():
            return 0

        for i in range(board.columns):
            if not board.columnIsFull(i) and board.wouldBeWin(i):
                return self.getScore(board, isMaximizingPlayer)

        if isMaximizingPlayer:
            best_score = -infinity
            for i in range(board.columns):
                if not board.columnIsFull(i):
                    column_index, row_index = board.insertPiece(i)
                    score = self.minimax(board, False)

                    board.fields[row_index][column_index] = None
                    board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                    best_score = max(best_score, score)
        else:
            best_score = infinity
            for i in range(board.columns):
                if not board.columnIsFull(i):
                    column_index, row_index = board.insertPiece(i)
                    score = self.minimax(board, True)

                    board.fields[row_index][column_index] = None
                    board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                    best_score = min(best_score, score)

        return best_score

    def solve(self, board):
        self.positionCount = 0
        if board.numberOfPiecesPlayed % 2 == 0:
            isMaximizingPlayer = True
        else:
            isMaximizingPlayer = False
        score = self.minimax(board, isMaximizingPlayer)
        return score if isMaximizingPlayer else -score

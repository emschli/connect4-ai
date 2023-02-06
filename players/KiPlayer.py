from math import inf as infinity
from minimax import minimax


class KiPlayer:
    def __init__(self):
        self.chosenColumn = None
        self.type = 'ki'

    def getMove(self, board, finish_event):
        isMaximizingPlayer = board.numberOfPiecesPlayed % 2 == 0
        best_score = -infinity if isMaximizingPlayer else infinity

        for i in range(board.columns):
            if not board.isColumnFull(i):
                column_index, row_index = board.insertPiece(i)

                score = minimax(board, column_index, row_index, isMaximizingPlayer)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                if (isMaximizingPlayer and score > best_score) or (not isMaximizingPlayer and score < best_score):
                    self.chosenColumn = column_index
                    best_score = score

        finish_event.set()

from math import inf as infinity
from negamax import Negamax


class KiPlayer:
    def __init__(self):
        self.chosenColumn = None
        self.type = 'ki'
        self.n = Negamax()

    def getMove(self, board, finish_event):
        best_score = -infinity

        for i in range(board.columns):
            if not board.columnIsFull(i):
                column_index, row_index = board.insertPiece(i)

                score = self.n.negamax(board)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                if score > best_score:
                    self.chosenColumn = column_index
                    best_score = score

        finish_event.set()

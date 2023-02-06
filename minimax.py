from math import inf as infinity


def getScore(board, isMaximizingPlayer):
    score = int((board.rows * board.columns + 2 - board.numberOfPiecesPlayed) / 2)
    return score if isMaximizingPlayer else -score


def minimax(board, lastMoveColumn, lastMoveRow, isMaximizingPlayer):
    if board.isWin(lastMoveColumn, lastMoveRow):
        return getScore(board, isMaximizingPlayer)
    elif board.isBoardFull():
        return 0
    else:
        best_score = -infinity if isMaximizingPlayer else infinity

        for i in range(board.columns):
            if not board.isColumnFull(i):
                column_index, row_index = board.insertPiece(i)

                score = minimax(board, column_index, row_index, not isMaximizingPlayer)

                board.fields[row_index][column_index] = None
                board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

                best_score = max(score, best_score) if isMaximizingPlayer else min(score, best_score)

        return best_score

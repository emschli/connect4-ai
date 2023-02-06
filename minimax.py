from math import inf as infinity


def getScore(board):
    return int((board.rows * board.columns - board.numberOfPiecesPlayed + 1) / 2)


def minimax(board):
    if board.isFull():
        return 0

    for i in range(board.columns):
        if not board.columnIsFull(i) and board.wouldBeWin(i):
            return getScore(board)

    best_score = -infinity

    for i in range(board.columns):
        if not board.columnIsFull(i):
            column_index, row_index = board.insertPiece(i)

            score = -minimax(board)

            board.fields[row_index][column_index] = None
            board.numberOfPiecesPlayed = board.numberOfPiecesPlayed - 1

            best_score = max(score, best_score)

    return best_score

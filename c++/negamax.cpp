#include "BitBoard.h"
#include "TranspositionTable.h"

#define ROWS 6
#define COLUMNS 7

const int explorationOrder[] = { 3, 2, 4, 5, 1, 0, 6 };

TranspositionTable *transpositionTable = new TranspositionTable(8388593);

int getScore(Bitboard *board) {
    return (ROWS * COLUMNS - board->numberOfPiecesPlayed + 2) / 2;
}

int recNegamax(Bitboard *board, int *positionCount, int alpha, int beta) {
    ++*positionCount;

    if (board->numberOfPiecesPlayed == Bitboard::WIDTH * Bitboard::HEIGHT) {
        return 0;
    }

    for (int i = 0; i < Bitboard::WIDTH; i++) {
        if (board->canPlay(i)) {
            board->insertPiece(i);
            if (board->isWin()) {
                int score = getScore(board);
                board->undoMove();
                return score;
            }
            board->undoMove();
        }

    }

    int maxScore = (COLUMNS * ROWS - 1 - board->numberOfPiecesPlayed) / 2;

    int valueFromTable = transpositionTable->get(board->getPositionCode());
    if (valueFromTable != 0) {
        maxScore = valueFromTable + Bitboard::MIN_SCORE - 1;
    }

    if (beta > maxScore) {
        beta = maxScore;
        if (alpha >= beta) {
            return beta;
        }
    }

    for (int move : explorationOrder) {
        if (board->canPlay(move)) {

            board->insertPiece(move);
            int score = -recNegamax(board, positionCount, -beta, -alpha);
            board->undoMove();

            if (score >= beta) {
                return score;
            }
            if (score > alpha) {
                alpha = score;
            }
        }
    }

    transpositionTable->put(board->getPositionCode(), alpha - Bitboard::MIN_SCORE +1);
    return alpha;
}

int negamax(long long *bitboards, int *heights, int *moves, int numberOfPiecesPlayed, int *positionCount) {
    Bitboard *board = new Bitboard(bitboards, heights, moves, numberOfPiecesPlayed);
    transpositionTable->reset();
    return recNegamax(board, positionCount, (-2147483647 - 1)+1, (2147483647));
}

extern "C" {
    int c_negamax(long long *bitboards, int *heights, int *moves, int numberOfPiecesPlayed, int *positionCount) { return negamax(bitboards, heights, moves, numberOfPiecesPlayed, positionCount); }
}
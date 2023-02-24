#include "BitBoard.h"
#include <bits/stdc++.h>
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

int negamax(long *bitboards, int *heights, int *moves, int numberOfPiecesPlayed, int *positionCount) {
    Bitboard *board = new Bitboard(bitboards, heights, moves, numberOfPiecesPlayed);
    transpositionTable->reset();
    return recNegamax(board, positionCount, INT32_MIN+1, INT32_MAX);
}

int main() {
//    long boards[] = {736375146669L, 13539960870674L};
//    int heights[] = {6, 13, 20, 27, 34, 40, 44};
//    int moves[42] = {1, 1, 4, 1, 4, 6, 5, 1, 4, 2, 3, 5, 1, 1, 3, 3, 0, 0, 0, 4, 5, 2, 2, 5, 4, 2, 3, 2, 5, 6, 0, 2, 4, 0, 3, 3, 0, -1, -1, -1, -1, -1};
//    int numberOfPiecesPlayed = 37;
//    int positionCount = 0;

//    long boards[] = {85111763436932L, 53409260683835L};
//    int heights[] = {6, 11, 20, 23, 34, 41, 47};
//    int moves[42] = {5, 4, 1, 0, 3, 5, 6, 2, 4, 4, 5, 0, 4, 4, 6, 2, 0, 4, 5, 5, 2, 0, 5, 2, 1, 6, 2, 6, 2, 1, 1, 0, 3, 0, 6, -1, -1, -1, -1, -1, -1, -1};
//    int numberOfPiecesPlayed = 35;
//    int positionCount = 0;

//    long boards[] = {0L, 0L};
//    int heights[] = {0, 7, 14, 21, 28, 35, 42};
//    int moves[42] = {};
//    int numberOfPiecesPlayed = 0;
//    int positionCount = 0;

    long boards[] = {13196287033605L, 17594065125506L};
    int heights[] = {3, 9, 16, 21, 32, 35, 45};
    int moves[42] = {2, 1, 6, 4, 0, 4, 6, 0, 1, 2, 0, 4, 4, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    int numberOfPiecesPlayed = 14;
    int positionCount = 0;

    int result = negamax(boards, heights, moves, numberOfPiecesPlayed, &positionCount);

    std::cout << result << std::endl;

    return 0;
}


extern "C" {
    int c_negamax(long *bitboards, int *heights, int *moves, int numberOfPiecesPlayed, int *positionCount) { return negamax(bitboards, heights, moves, numberOfPiecesPlayed, positionCount); }
}
#include "BitBoard.h"
#include <bits/stdc++.h>
#include "TranspositionTable.h"

#define ROWS 6
#define COLUMNS 7

const int explorationOrder[] = { 3, 2, 4, 5, 1, 0, 6 };
//TODO: Pass in reference to struct vector from python
TranspositionTable *transpositionTable = new TranspositionTable(8388593);

int getScore(Bitboard *board) {
    return (ROWS * COLUMNS - board->numberOfPiecesPlayed +2) / 2;
}

bool contains(std::vector<int> *list, int element) {
    for (int i : *list) {
        if (i == element) {
            return true;
        }
    }
    return false;
}

int recNegamax(Bitboard *board, int *positionCount, int alpha, int beta) {
    ++*positionCount;

    std::vector<int> possibleMoves = board->getPossibleMoves();

    if (possibleMoves.empty()) {
        return 0;
    }

    for (int move : possibleMoves) {
        board->insertPiece(move);
        if (board->isWin()) {
            int score = getScore(board);
            board->undoMove();
            return score;
        }
        board->undoMove();
    }

    int maxScore = (COLUMNS * ROWS - 1 - board->numberOfPiecesPlayed) / 2;

    int valueFromTable = transpositionTable->get(board->getPositionCode());
    if (valueFromTable != 0) {
        maxScore = valueFromTable +  Bitboard::MIN_SCORE - 1; //TODO: Why??
    }

    if (beta > maxScore) {
        beta = maxScore;
        if (alpha >= beta) {
            return beta;
        }
    }

    for (int move : explorationOrder) {
        //TODO: contains kann effizienter gemacht werden dank heights[]
        if (contains(&possibleMoves, move)) {

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
    long boards[] = {736375146669L, 13539960870674L};
    int heights[] = {6, 13, 20, 27, 34, 40, 44};
    int moves[42] = {1, 1, 4, 1, 4, 6, 5, 1, 4, 2, 3, 5, 1, 1, 3, 3, 0, 0, 0, 4, 5, 2, 2, 5, 4, 2, 3, 2, 5, 6, 0, 2, 4, 0, 3, 3, 0, -1, -1, -1, -1, -1};
    int numberOfPiecesPlayed = 37;
    int positionCount = 0;
//    long boards[] = {85111763436932L, 53409260683835L};
//    int heights[] = {6, 11, 20, 23, 34, 41, 47};
//    int moves[42] = {5, 4, 1, 0, 3, 5, 6, 2, 4, 4, 5, 0, 4, 4, 6, 2, 0, 4, 5, 5, 2, 0, 5, 2, 1, 6, 2, 6, 2, 1, 1, 0, 3, 0, 6, -1, -1, -1, -1, -1, -1, -1};
//    int numberOfPiecesPlayed = 35;
//    int positionCount = 0;

    int result = negamax(boards, heights, moves, numberOfPiecesPlayed, &positionCount);

    std::cout << result << std::endl;

    return 0;
}


extern "C" {
    int c_negamax(long *bitboards, int *heights, int *moves, int numberOfPiecesPlayed, int *positionCount) { return negamax(bitboards, heights, moves, numberOfPiecesPlayed, positionCount); }
}
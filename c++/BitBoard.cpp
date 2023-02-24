#include "BitBoard.h"

using namespace std;

const int directions[] = {1, 7, 6, 8};

Bitboard::Bitboard(long *boards, int *heights, int *moves, int numberOfPiecesPlayed) {
    this->boards = boards;
    this->heights = heights;
    this->moves = moves;
    this->numberOfPiecesPlayed = numberOfPiecesPlayed;
}

void Bitboard::insertPiece(int columnIndex) {
    long move = 1L << this->heights[columnIndex]++;
    this->boards[this->numberOfPiecesPlayed & 1] ^= move;
    this->moves[numberOfPiecesPlayed++] = columnIndex;
}

void Bitboard::undoMove() {
    int columnIndex = this->moves[--this->numberOfPiecesPlayed];
    long move = 1L << --this->heights[columnIndex];
    this->boards[this->numberOfPiecesPlayed & 1] ^= move;
}

bool Bitboard::isWin() {
    long board = this->boards[(numberOfPiecesPlayed-1) & 1];
    for (int direction: directions) {
        if ((board & (board >> direction) & (board >> 2 * direction) & (board >> 3 * direction)) != 0) {
            return true;
        }
    }
    return false;
}

long Bitboard::getPositionCode() {
    return 2 * boards[0] + boards[1] + TOP_MASK;
}

bool Bitboard::canPlay(int column) {
    long pretendedMove = 1L << this->heights[column];
    return (TOP_MASK & pretendedMove) == 0;
}
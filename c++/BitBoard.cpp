#include "BitBoard.h"

using namespace std;

const int directions[] = {1, 7, 6, 8};
const int SIZE1 = 7*7;
const long ALL1 = (1L << (SIZE1))-1L;
const int COL1 = (1 << 7) - 1;
const long BOTTOM = ALL1 / COL1;

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

std::vector<int> Bitboard::getPossibleMoves() {
    long top = 0b1000000100000010000001000000100000010000001000000L;
    std::vector<int> result;

    for (int i = 0; i <= 6; i++) {
        long pretendedMove = 1L << this->heights[i];
        if ((top & pretendedMove) == 0) {
            result.push_back(i);
        }
    }

    return result;
}

long Bitboard::getPositionCode() {
    return 2 * boards[0] + boards[1] + BOTTOM;
}
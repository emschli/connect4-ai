//
// Created by mirjam on 15.02.23.
//
#include <vector>


class Bitboard {
public:
    int numberOfPiecesPlayed;

    Bitboard(long *boards, int *heights, int *moves, int numberOfPiecesPlayed);

    void insertPiece(int columnIndex);

    void undoMove();

    bool isWin();

    std::vector<int> getPossibleMoves();

private:
    long *boards;
    int *heights;
    int *moves;
};
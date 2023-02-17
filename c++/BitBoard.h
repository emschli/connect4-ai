#include <vector>

class Bitboard {
public:
    static const int MIN_SCORE = -(7*6) / 2 +3;

    int numberOfPiecesPlayed;

    Bitboard(long *boards, int *heights, int *moves, int numberOfPiecesPlayed);

    void insertPiece(int columnIndex);

    void undoMove();

    bool isWin();

    std::vector<int> getPossibleMoves();

    long getPositionCode();

private:
    long *boards;
    int *heights;
    int *moves;
};
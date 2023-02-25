class Bitboard {
public:
    static const int MIN_SCORE = -(7*6) / 2 +3;
    static const int WIDTH = 7;
    static const int HEIGHT = 6;

    int numberOfPiecesPlayed;

    Bitboard(long long *boards, int *heights, int *moves, int numberOfPiecesPlayed);

    void insertPiece(int columnIndex);

    void undoMove();

    bool isWin();

    bool canPlay(int column);

    long long getPositionCode();

private:
    long long *boards;
    int *heights;
    int *moves;
    static const long long TOP_MASK = 0b1000000100000010000001000000100000010000001000000L;
};
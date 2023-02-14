from Board import ONGOING, DRAW, WIN


class BitBoard:
    def __init__(self):
        self.boards = [0, 0]
        self.height = [0, 7, 14, 21, 28, 35, 42]
        self.moves = []
        self.rows = 6
        self.columns = 7
        self.numberOfPiecesPlayed = 0
        self.directions = [1, 7, 6, 8]

    def insertPiece(self, columnIndex):
        move = 1 << self.height[columnIndex]
        self.height[columnIndex] += 1

        self.boards[self.numberOfPiecesPlayed & 1] ^= move

        self.moves.append(columnIndex)
        self.numberOfPiecesPlayed += 1

    def undoMove(self):
        self.numberOfPiecesPlayed -= 1
        column_index = self.moves[self.numberOfPiecesPlayed]

        self.height[column_index] -= 1
        move = 1 << self.height[column_index]
        self.boards[self.numberOfPiecesPlayed & 1] ^= move

    def isWin(self):
        board = self.boards[(self.numberOfPiecesPlayed-1) & 1]
        for direction in self.directions:
            if board & (board >> direction) & (board >> 2 * direction) & (board >> 3 * direction) != 0:
                return True
        return False

    def getPossibleMoves(self):
        result = []
        top = 0b1000000_1000000_1000000_1000000_1000000_1000000_1000000

        for i in range(self.columns):
            pretended_move = 1 << self.height[i]
            if top & pretended_move == 0:
                result.append(i)

        return result

    def getArrayBoard(self):
        result = []
        bit_string_player_1 = self._sanitizeBitString(self.boards[0])
        bit_string_player_2 = self._sanitizeBitString(self.boards[1])

        start_index = 5
        end_index = 48
        for i in range(6):
            row = []
            for j in range(start_index, end_index, 7):
                if bit_string_player_1[j] == '1':
                    row.append(True)
                elif bit_string_player_2[j] == '1':
                    row.append(False)
                else:
                    row.append(None)
            result.append(row)
            start_index -= 1
            end_index -= 1

        return result

    def _sanitizeBitString(self, bitBoard):
        s = format(bitBoard, '#050b')
        s = s.removeprefix('0b')
        s = s[::-1]
        return s

    def insertPieceWithWinCalc(self, column):
        self.insertPiece(column)

        if self.isWin():
            return WIN
        elif not self.getPossibleMoves():
            return DRAW
        else:
            return ONGOING

    @staticmethod
    def createBoardFromString(string):
        board = BitBoard()
        for c in string:
            column = int(c)
            board.insertPiece(column - 1)

        return board

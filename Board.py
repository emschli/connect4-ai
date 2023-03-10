import numpy as np

ONGOING = 'X'

DRAW = 'DRAW'

WIN = 'WIN'

ROWS = 6
COLUMNS = 7


class Board:
    starting_player_symbol = True

    def __init__(self, rows=ROWS, columns=COLUMNS):
        self.fields = np.array([[None] * columns for _ in range(rows)])
        self.rows = rows
        self.columns = columns
        self.numberOfPiecesPlayed = 0

    def insertPiece(self, columnIndex):
        column = self.fields[:, columnIndex]
        assert column[0] is None, "Column must not be Full"

        res = list(filter(lambda f: f is None, column))
        row_index = len(res) - 1

        if self.numberOfPiecesPlayed % 2 == 0:
            symbol = self.starting_player_symbol
        else:
            symbol = not self.starting_player_symbol

        self.fields[row_index, columnIndex] = symbol
        self.numberOfPiecesPlayed = self.numberOfPiecesPlayed + 1

        return columnIndex, row_index

    def insertPieceWithWinCalc(self, columnIndex):
        row_index = self.insertPiece(columnIndex)[1]

        if self.isWin(columnIndex, row_index):
            return WIN
        elif self.isFull():
            return DRAW
        else:
            return ONGOING

    def isFull(self):
        return self.numberOfPiecesPlayed == self.rows * self.columns

    def isWin(self, columnIndex, rowIndex):
        lines = []
        lines.append(self.fields[:, columnIndex])
        lines.append(self.fields[rowIndex])
        diagonals = self._getDiagonals(columnIndex, rowIndex)
        lines.append(diagonals[0])
        lines.append(diagonals[1])

        for line in lines:
            if self._4connected(line):
                return True

        return False

    def wouldBeWin(self, column):
        column_index, row_index = self.insertPiece(column)
        win = self.isWin(column_index, row_index)
        self.fields[row_index][column_index] = None
        self.numberOfPiecesPlayed = self.numberOfPiecesPlayed - 1
        return win

    def _getDiagonals(self, columnIndex, rowIndex):
        main_diagonal = []
        second_diagonal = []

        i = rowIndex-1
        j = columnIndex-1
        main_diagonal_upper_part = []
        while i >= 0 and j >= 0:
            main_diagonal_upper_part.append(self.fields[i, j])
            i = i-1
            j = j-1
        main_diagonal_upper_part.reverse()
        main_diagonal.extend(main_diagonal_upper_part)
        main_diagonal.append(self.fields[rowIndex, columnIndex])

        i = rowIndex+1
        j = columnIndex+1
        while i < self.rows and j < self.columns:
            main_diagonal.append(self.fields[i, j])
            i = i+1
            j = j+1

        #second Diagonal
        second_diagonal_lower_part = []
        i = rowIndex+1
        j = columnIndex-1
        while i < self.rows and j >= 0:
            second_diagonal_lower_part.append(self.fields[i, j])
            i = i+1
            j = j-1
        second_diagonal_lower_part.reverse()
        second_diagonal.extend(second_diagonal_lower_part)
        second_diagonal.append(self.fields[rowIndex, columnIndex])

        i = rowIndex-1
        j = columnIndex+1
        while i >= 0 and j < self.columns:
            second_diagonal.append(self.fields[i, j])
            i = i-1
            j = j+1

        return main_diagonal, second_diagonal

    def _4connected(self, line):
        count = 0
        index = 0
        currentSymbol = None

        while count < 4 and index < len(line):
            f = line[index]

            if f is None:
                currentSymbol = None
                count = 0
            elif f is not currentSymbol:
                count = 1
                currentSymbol = f
            else:
                count = count+1

            index = index+1

        return True if count == 4 else False

    def columnIsFull(self, columnIndex):
        return self.fields[:, columnIndex][0] is not None

    def getArrayBoard(self):
        return self.fields

    @staticmethod
    def createBoardFromString(string):
        board = Board()
        for c in string:
            column = int(c)
            board.insertPiece(column-1)

        return board

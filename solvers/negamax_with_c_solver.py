from math import inf as infinity
from BitBoard import BitBoard
from ctypes import c_int, c_longlong, cdll, byref
from rootPath import root_path
import os


class NegamaxWithCSolver:
    version = '_v5'
    default_board = BitBoard

    def __init__(self):
        self.positionCount = 0
        self.explorationOrder = [3, 2, 4, 5, 1, 0, 6]
        pathToLib = os.path.join(root_path , 'c++', 'libnegamax.so')
        self.lib = cdll.LoadLibrary(pathToLib)
        self.lib.c_negamax.restype = c_int

    def solve(self, board):
        c_positionCount= c_int()
        c_boards = (c_longlong * 2)(*board.boards)
        c_heights = (c_int * board.columns)(*board.height)
        c_moves = (c_int * 42)(*board.moves)
        score = self.lib.c_negamax(byref(c_boards), byref(c_heights), byref(c_moves), board.numberOfPiecesPlayed, byref(c_positionCount))
        self.positionCount = c_positionCount.value
        return score

    def getBestMove(self, board):
        best_score = -infinity
        chosen_column = None

        for i in board.getPossibleMoves():
            board.insertPiece(i)

            score = -self.solve(board)

            board.undoMove()

            if score > best_score:
                chosen_column = i
                best_score = score

        return chosen_column

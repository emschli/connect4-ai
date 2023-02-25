from config import solver


class KiPlayer:
    def __init__(self):
        self.type = 'ki'
        self.solver = solver
        self.chosenColumn = None
        self.defaultBoard = solver.default_board

    def getMove(self, board, finish_event):
        self.chosenColumn = solver.getBestMove(board)
        finish_event.set()

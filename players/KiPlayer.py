from config import solver


class KiPlayer:
    def __init__(self):
        self.type = 'ki'
        self.solver = solver
        self.defaultBoard = solver.default_board

    def getMove(self, board, finish_event, r_value):
        r_value.value = solver.getBestMove(board)
        finish_event.set()

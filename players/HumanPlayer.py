

class HumanPlayer:
    def __init__(self):
        self.chosenColumn = None
        self.type = 'human'

    def getMove(self, board, finish_event):
        while True:
            try:
                player_input = int(input('Choose Number of Column: \n'))
                if 0 <= player_input <= board.columns:
                    self.chosenColumn = player_input
                    break
            except Exception as e:
                pass
        finish_event.set()

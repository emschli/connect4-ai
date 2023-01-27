

class HumanPlayer:
    def getMove(self, board):
        while True:
            chosenColumn = int(input('Choose Number of Column: \n'))
            if chosenColumn >= 0 and chosenColumn <= board.columns:
                return chosenColumn
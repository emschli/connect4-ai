from players.HumanPlayer import HumanPlayer
from VisualGame import VisualGame

humanPlayer1 = HumanPlayer()
humanPlayer2 = HumanPlayer()

game = VisualGame(humanPlayer1, humanPlayer2)
game.play()
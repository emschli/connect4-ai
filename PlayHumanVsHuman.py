from players.HumanPlayer import HumanPlayer
from VisualGame import VisualGame
from BitBoard import BitBoard

humanPlayer1 = HumanPlayer()
humanPlayer2 = HumanPlayer()

board = BitBoard()
game = VisualGame(humanPlayer1, humanPlayer2, board)
game.play()

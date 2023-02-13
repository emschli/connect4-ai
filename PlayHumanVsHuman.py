from players.HumanPlayer import HumanPlayer
from VisualGame import VisualGame
from Board import Board

humanPlayer1 = HumanPlayer()
humanPlayer2 = HumanPlayer()

board = Board()
game = VisualGame(humanPlayer1, humanPlayer2, board)
game.play()

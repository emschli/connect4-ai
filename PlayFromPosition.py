from Board import Board
from BitBoard import BitBoard
from players.HumanPlayer import HumanPlayer
from VisualGame import VisualGame

board_string = '6763525635134453444361412671365712'

board = BitBoard.createBoardFromString(board_string)
player1 = HumanPlayer()
player2 = HumanPlayer()
game = VisualGame(player1, player2, board)
game.play()

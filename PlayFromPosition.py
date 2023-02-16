from Board import Board
from BitBoard import BitBoard
from players.HumanPlayer import HumanPlayer
from VisualGame import VisualGame

board_string = '65214673556155731566316327373221417'

board = BitBoard.createBoardFromString(board_string)
player1 = HumanPlayer()
player2 = HumanPlayer()
game = VisualGame(player1, player2, board)
game.play()

from Board import Board
from players.HumanPlayer import HumanPlayer
from players.KiPlayer import KiPlayer
from VisualGame import VisualGame

board_string = '2252576253462244111563365343671351441'

board = Board.createBoardFromString(board_string)
player1 = KiPlayer()
player2 = HumanPlayer()
game = VisualGame(player1, player2, board)
game.play()

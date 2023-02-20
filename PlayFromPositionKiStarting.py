from players.HumanPlayer import HumanPlayer
from players.KiPlayer import KiPlayer
from VisualGame import VisualGame

board_string = '2416615552'

ki_player = KiPlayer()
human_player = HumanPlayer()
board = ki_player.defaultBoard.createBoardFromString(board_string)
game = VisualGame(ki_player, human_player, board)
game.play()

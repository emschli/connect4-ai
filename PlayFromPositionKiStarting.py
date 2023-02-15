from players.HumanPlayer import HumanPlayer
from players.KiPlayer import KiPlayer
from VisualGame import VisualGame

board_string = '6763525635134453444361412671365712'

ki_player = KiPlayer()
human_player = HumanPlayer()
board = ki_player.defaultBoard.createBoardFromString(board_string)
game = VisualGame(ki_player, human_player, board)
game.play()

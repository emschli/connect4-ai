from players.HumanPlayer import HumanPlayer
from players.KiPlayer import KiPlayer
from VisualGame import VisualGame

board_string = '2252576253462244111563365343671351441'

ki_player = KiPlayer()
human_player = HumanPlayer()
board = ki_player.defaultBoard.createBoardFromString(board_string)
game = VisualGame(ki_player, human_player, board)
game.play()

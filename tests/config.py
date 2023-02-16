from solvers.minimax import Minimax
from solvers.negamax import Negamax
from solvers.negamax_alpha_beta import NegamaxAlphaBeta
from solvers.negamax_alpha_beta_move_ordering import NegamaxAlphaBetaMoveOrdering
from solvers.negamax_with_bitboard import NegamaxWithBitboard
from solvers.negamax_with_c_solver import NegamaxWithCSolver


# solver = Minimax()
# solver = Negamax()
# solver = NegamaxAlphaBeta()
# solver = NegamaxAlphaBetaMoveOrdering()
# solver = NegamaxWithBitboard()
solver = NegamaxWithCSolver()

from config import solver
import time
from BitBoard import BitBoard

board = BitBoard()
start = time.process_time()
result = solver.solve(board)
end = time.process_time()
duration = end - start
print("Result: " + str(result))
print("Duration: " + str(duration) + "s")

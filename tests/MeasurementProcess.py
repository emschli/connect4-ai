from multiprocessing import Process
import os
from config import solver
import time

wd = os.getcwd()
complete_path = wd + '/measurements/'


class MeasurementProcess(Process):
    def __init__(self, testBoards, filename):
        super().__init__()
        self.boards = testBoards
        self.filePath = complete_path+filename

    def run(self):
        try:
            os.remove(self.filePath)
        except OSError:
            pass

        for i, board_and_score in enumerate(self.boards):
            board = board_and_score[0]

            start = time.process_time_ns()
            solver.solve(board)
            end = time.process_time_ns()
            duration = end - start
            pos_count = solver.positionCount

            line = str(i+1), str(duration), str(pos_count)
            line_to_write = " ".join(line) + "\n"
            with open(self.filePath, 'a+') as writer:
                writer.write(line_to_write)

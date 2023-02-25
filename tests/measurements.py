from importTestBoards import readFile, END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
from MeasurementProcess import MeasurementProcess
from config import solver

fileNames = END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
version = solver.version
seconds_to_sleep = 60 * 5

if __name__ == '__main__':
    for i in range(6):
        fileName = fileNames[i]
        print('Starting Measurements for: ' + fileName)

        test_boards = readFile(fileName)
        process = MeasurementProcess(test_boards, fileName+version)

        process.start()
        process.join(seconds_to_sleep)

        if process.is_alive():
            process.kill()

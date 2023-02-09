from importTestBoards import readFile, END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
from MeasurementProcess import MeasurementProcess
import time
from negamax import Negamax

fileNames = END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
version = Negamax.version
#TODO: auf sinnvolle Zeit festlegen
seconds_to_sleep = 60

for i in range(6):
    fileName = fileNames[i]
    print('Starting Measurements for: ' + fileName)

    test_boards = readFile(fileName)
    process = MeasurementProcess(test_boards, fileName+version)

    process.start()
    time.sleep(seconds_to_sleep)

    if process.is_alive():
        process.kill()

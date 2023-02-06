import os
from Board import Board

wd = os.getcwd()
complete_path = wd + '/testStrings/'

END_EASY = '1_end-easy'
MIDDLE_EASY = '2_middle-easy'
MIDDLE_MEDIUM = '3_middle-medium'
BEGIN_EASY = '4_begin-easy'
BEGIN_MEDIUM = '5_begin-medium'
BEGIN_HARD = '6_begin-hard'


def readFile(fileName):
    result = []
    with open(complete_path+fileName, 'r') as reader:
        line = reader.readline()
        while line != '':
            splitted_line = line.split()
            board = Board.createBoardFromString(splitted_line[0])
            result.append((board, int(splitted_line[1])))
            line = reader.readline()
    return result

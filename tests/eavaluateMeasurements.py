from importTestBoards import END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
import os

fileNames = END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
namesInTable = [
    "Ende leicht",
    "Mitte leicht",
    "Mitte mittelschwer",
    "Anfang leicht",
    "Anfang mittelschwer",
    "Anfang schwer"
]
version = '_v2'
base_path = os.getcwd() + '/measurements/'
base_path_evaluations = base_path + 'evaluations/'
full_evaluation_path = base_path_evaluations + 'eval' + version

try:
    os.remove(full_evaluation_path)
except OSError:
    pass

for i, fileName in enumerate(fileNames):
    full_file_path = base_path + fileName + version
    duration_sum = 0
    nodes_explored_sum = 0
    number_of_boards = 0

    if os.path.isfile(full_file_path):
        with open(full_file_path, 'r') as reader:
            line = reader.readline()

            while line != '':
                _, duration, nodes_count = line.split(" ")
                number_of_boards += 1
                duration_sum += int(duration)
                nodes_explored_sum += int(nodes_count)
                line = reader.readline()

        mean_duration = duration_sum / number_of_boards
        mean_nodes_explored = nodes_explored_sum / number_of_boards
        percentage_of_boards_solved = (number_of_boards / 1000) * 100
        summary = (
            namesInTable[i],
            str(round(percentage_of_boards_solved, 2)) + '\\%',
            str(round(mean_duration / 1_000_000, 2)),
            str(round(mean_nodes_explored, 2))
        )

        line_for_table = " & ".join(summary) + ' \\\\\n'

    else:
        summary = (
            namesInTable[i],
            "0.0\\%",
            "-",
            "-"
        )
        line_for_table = " & ".join(summary) + ' \\\\\n'

    with open(full_evaluation_path, 'a+') as writer:
        writer.write(line_for_table)

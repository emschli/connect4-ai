import matplotlib.pyplot as plt
from importTestBoards import END_EASY, MIDDLE_EASY, MIDDLE_MEDIUM, BEGIN_EASY, BEGIN_MEDIUM, BEGIN_HARD
import os
from eavaluateMeasurements import fileNames
import statistics

measurement = 'duration'
# measurement = 'nodeCount'

versions = [
    '_v0',
    '_v1',
    '_v2',
    '_v3',
    '_v4'
]

results = {
    END_EASY: [],
    MIDDLE_EASY: [],
    MIDDLE_MEDIUM: [],
    BEGIN_EASY: [],
    BEGIN_MEDIUM: [],
    BEGIN_HARD: []
}
measurements_path = os.getcwd() + '/measurements/'
evaluation_path = measurements_path + 'evaluations/' + measurement + '_overview.png'


def getMeanDuration(pathToFile):
    values = []
    with open(pathToFile, 'r') as reader:
        line = reader.readline()

        while line != '':
            _, duration, nodes_count = line.split(" ")
            values.append(int(duration))
            line = reader.readline()

    return statistics.mean(values)


def getMeanNodesCount(pathToFile):
    values = []
    with open(pathToFile, 'r') as reader:
        line = reader.readline()

        while line != '':
            _, duration, nodes_count = line.split(" ")
            values.append(int(nodes_count))
            line = reader.readline()

    return statistics.mean(values)


try:
    os.remove(evaluation_path)
except OSError:
    pass

for testCase in fileNames:
    l = results[testCase]

    for version in versions:
        path = measurements_path + testCase + version

        if os.path.isfile(path):
            if measurement == 'duration':
                mean = getMeanDuration(path)
            else:
                mean = getMeanNodesCount(path)

            l.append((version, mean))

figure, ax = plt.subplots()

for key, result in results.items():
    if result:
        x = list(map(lambda tup: tup[0], result))
        y = list(map(lambda tup: tup[1], result))
        plt.plot(x, y, label=key)

plt.legend()
ax.set(title=measurement)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos: format(x/1000,'1.0f')+'K'))
figure.savefig(evaluation_path)
plt.show()

# Requirements:
* Python 3
* pip
* g++

# First steps

1. run `pip install -r requirements.txt` from project root project folder
2. Build C++ Part (run all from `./c++` folder):
   1. `g++ -c -fPIC negamax.cpp BitBoard.cpp TranspositionTable.cpp`
   2. `g++ -shared negamax.o BitBoard.o TranspositionTable.o -o libnegamax_ts.so`

# Spielen gegen die Vier gewinnt Ki

Durch Ausführen der Datei `PlayFromPositionKiStarting.py` kann gegen die KI gespielt werden.
Die Startposition ist bestimmt durch den String `board_string`.
Im Ordner `./tests/testStrings` befinden sich weitere Spielpositions-Strings.

In der Datei `config.py` kann zwischen den verschiedenen Versionen des Solvers gewechselt werden.
Der C++-Solver ohne Transposition Table kann möglicher Weise nicht verwendet werden, da die Library nur einmal für meinen Rechner kompiliert wurde.
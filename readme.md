# Requirements:
* Python 3
* pip
* cmake

# First steps

1. run `pip install -r requirements.txt` from project root project folder
2. run `cmake .` and `cmake -- build .` from `./c++` folder


# Spielen gegen die Vier gewinnt Ki

Durch Ausführen der Datei `PlayFromPositionKiStarting.py` kann gegen die KI gespielt werden.
Die Startposition ist bestimmt durch den String `board_string`.
Im Ordner `./tests/testStrings` befinden sich weitere Spielpositions-Strings.

In der Datei `config.py` kann zwischen den verschiedenen Versionen des Solvers gewechselt werden.
Der C++-Solver ohne Transposition Table kann möglicher Weise nicht verwendet werden, da Library nur einmal für meinen Rechner kompiliert wurde.
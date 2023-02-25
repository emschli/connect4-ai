cmake_minimum_required(VERSION 3.16.3)
project(c__)

set(CMAKE_CXX_STANDARD 17)
set(PROJECT_HEADERS
        BitBoard.h
        TranspositionTable.h)
set(PROJECT_SOURCES
        negamax.cpp
        BitBoard.cpp
        TranspositionTable.cpp)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY .)
add_library(negamax_ts SHARED negamax.cpp BitBoard.h BitBoard.cpp TranspositionTable.cpp TranspositionTable.h)

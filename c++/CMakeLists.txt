cmake_minimum_required(VERSION 3.24)
project(c__)

set(CMAKE_CXX_STANDARD 17)
set(PROJECT_HEADERS
        BitBoard.h
        )
set(PROJECT_SOURCES
        negamax.cpp
        BitBoard.cpp
        )

add_executable(untitled1 ${PROJECT_SOURCES} ${PROJECT_HEADERS})

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ../)
add_library(negamax SHARED negamax.cpp BitBoard.h BitBoard.cpp)

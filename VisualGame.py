import pygame
import threading
from Board import Board, ONGOING

SIZE_OF_FIELD = 50
DIAMETER = SIZE_OF_FIELD - 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
YELLOW = (255, 255, 102)


class Quit(Exception):
    pass


class VisualGame:
    def __init__(self, startingPlayer, secondPlayer, board=Board()):
        pygame.init()
        self.displayHeight = board.rows * SIZE_OF_FIELD
        self.displayWidth = board.columns * SIZE_OF_FIELD
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('Connect 4')
        self.startingPlayer = startingPlayer
        self.secondPlayer = secondPlayer
        self.board = board
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.kiThread = None
        self.columnBorders = self._initColumnBorders(board.columns)

    def _initColumnBorders(self, columns):
        borders = []
        for i in range(columns):
            borders.append(i*SIZE_OF_FIELD)
        return borders

    def play(self):
        gameFinished = False
        currentPlayer = self.startingPlayer
        self._drawBoard()
        pygame.display.flip()

        status = None
        try:
            while not gameFinished:
                if currentPlayer.type == 'human':
                    column = self._makeHumanMove()
                else:
                    column = self._makeKiMove(currentPlayer)

                resultOfMove = self.board.playPiece(column)
                status = resultOfMove[0]
                self._drawBoard()
                pygame.display.flip()
                currentPlayer = self._getNextPlayer(currentPlayer)
                gameFinished = self._isGameFinished(resultOfMove)

            self._printGameFinishedMessage(status)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        raise Quit
        except Quit:
            try:
                pygame.quit()
            except pygame.error:
                print('Quit!')
            finally:
                if self.kiThread is not None:
                    self.kiThread.terminate()
                exit()

    def _makeHumanMove(self):
        while True:
            self._drawBoard()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            column = self._getColumnForMousePosition(mouse_x)
            rect = self._createRectangleFrame(column)
            pygame.draw.rect(self.display, BLACK, rect, 4)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise Quit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return column

    def _createRectangleFrame(self, column):
        rect_x_pos = self.columnBorders[column]
        rect_y_pos = 0
        rect_width = SIZE_OF_FIELD
        rect_height = SIZE_OF_FIELD * self.displayHeight
        return pygame.Rect(rect_x_pos, rect_y_pos, rect_width, rect_height)

    def _getColumnForMousePosition(self, mouse_x):
        indices = [i for i in range(self.board.columns)]
        indices.reverse()

        for columnIndex in indices:
            if mouse_x >= self.columnBorders[columnIndex]:
                return columnIndex

    def _makeKiMove(self, currentPlayer):
        finish_event = threading.Event()
        self.kiThread = threading.Thread(target=currentPlayer.getMove, args=(self.board, finish_event))
        self.kiThread.start()

        while not finish_event.is_set():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise Quit
        return  currentPlayer.chosenColumn

    def _printGameFinishedMessage(self, status):
        if status == 'DRAW':
            message = 'DRAW!'
        else:
            if self.board.numberOfPiecesPlayed % 2 != 0:
                color = 'Red'
            else:
                color = 'Yellow'
            message = color + ' wins!'

        print_message = self.font_style.render(message, True, BLACK)
        self.display.blit(print_message, [self.displayWidth / 2, self.displayHeight / 2])
        pygame.display.update()

    def _drawBoard(self):
        self.display.fill(WHITE)
        for i in range(self.board.rows):
            for j in range(self.board.columns):
                field = self.board.fields[i, j]
                if field is not None:
                    x = j * SIZE_OF_FIELD + 0.5 * SIZE_OF_FIELD
                    y = i * SIZE_OF_FIELD + 0.5 * SIZE_OF_FIELD

                    if field is True:
                        pygame.draw.circle(self.display, RED, (x, y), DIAMETER)
                    else:
                        pygame.draw.circle(self.display, YELLOW, (x, y), DIAMETER)

    def _getNextPlayer(self, currentPlayer):
        if currentPlayer == self.startingPlayer:
            return self.secondPlayer
        else:
            return self.startingPlayer

    def _isGameFinished(self, resultOfMove):
        if resultOfMove[0] == ONGOING:
            return False
        else:
            return True

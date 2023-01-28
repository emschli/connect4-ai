import pygame
import threading
from Board import Board, ONGOING

SIZE_OF_FIELD = 50
DIAMETER = SIZE_OF_FIELD - 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
YELLOW = (255, 255, 102)


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

    def play(self):
        gameFinished = False
        currentPlayer = self.startingPlayer
        self._drawBoard()

        class Quit(Exception):
            pass

        status = None
        try:
            while not gameFinished:
                finish_event = self._startGetMoveThread(currentPlayer)

                while not finish_event.is_set():
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            raise Quit

                column = currentPlayer.chosenColumn
                resultOfMove = self.board.playPiece(column)
                status = resultOfMove[0]
                self._drawBoard()
                currentPlayer = self._getNextPlayer(currentPlayer)
                gameFinished = self._isGameFinished(resultOfMove)

            self._printGameFinishedMessage(currentPlayer, status)

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
                exit()

    def _printGameFinishedMessage(self, currentPlayer, status):
        if status == 'DRAW':
            message = 'DRAW!'
        else:
            lastMovedPlayer = self._getNextPlayer(currentPlayer)
            if lastMovedPlayer == self.startingPlayer:
                color = 'Red'
            else:
                color = 'Yellow'
            message = color + ' wins!'

        print_message = self.font_style.render(message, True, BLACK)
        self.display.blit(print_message, [self.displayWidth / 2, self.displayHeight / 2])
        pygame.display.update()

    def _startGetMoveThread(self, currentPlayer):
        finish_event = threading.Event()

        if currentPlayer.type == 'human':
            args = (self.board, finish_event)
        else:
            args = ()

        thread = threading.Thread(target=currentPlayer.getMove, args=args)
        thread.start()
        return finish_event


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
        pygame.display.update()

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

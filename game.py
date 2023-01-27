from const import *
import pygame


class Game:
    def __init__(self):
        self.next_player = 0
        self.x_clicked = []
        self.o_clicked = []
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def check(self):
        # rows
        for i in range(3):
            if {(i, 0), (i, 1), (i, 2)}.issubset(self.o_clicked): return 'o'
            if {(0, i), (1, i), (2, i)}.issubset(self.o_clicked): return 'o'
            if {(i, 0), (i, 1), (i, 2)}.issubset(self.x_clicked): return 'x'
            if {(0, i), (1, i), (2, i)}.issubset(self.x_clicked): return 'x'
        if {(0, 0), (1, 1), (2, 2)}.issubset(self.o_clicked): return 'o'
        if {(0, 2), (1, 1), (2, 0)}.issubset(self.o_clicked): return 'o'
        if {(0, 0), (1, 1), (2, 2)}.issubset(self.x_clicked): return 'x'
        if {(0, 2), (1, 1), (2, 0)}.issubset(self.x_clicked): return 'x'
        return None

    def game_state(self):
        if len(self.o_clicked) + len(self.x_clicked) < 9:
            if self.check() is not None:
                return self.check()
        else:
            if self.check() is not None:
                return self.check()
            return 'draw'
        return None

    #check is game over -- return bool
    def game_over(self):
        if self.game_state() is not None:
            return True
        return False

    
    #update board and o_clicked x_clicked array
    def update(self, clicked):
        if self.next_player == 0:
            if clicked not in self.x_clicked and clicked not in self.o_clicked:
                self.o_clicked.append(clicked)
                self.next_turn()
        else:
            if clicked not in self.x_clicked and clicked not in self.o_clicked:
                self.x_clicked.append(clicked)
                self.next_turn()
        self.update_board()

    #next turn
    def next_turn(self):
        self.next_player = 1 if self.next_player == 0 else 0

    #draw o and cross and background
    def draw_(self, screen):
        for i in range(len(self.o_clicked)):
            pygame.draw.circle(screen, 'black', (
                self.o_clicked[i][0] * SQUARE_SIZE + WIDTH / 2 - SQUARE_SIZE,
                self.o_clicked[i][1] * SQUARE_SIZE + HEIGHT / 2 - SQUARE_SIZE), 90,
                               width=20)
        for i in range(len(self.x_clicked)):
            pygame.draw.line(screen, 'black',
                             (
                                 self.x_clicked[i][0] * SQUARE_SIZE + WIDTH / 2 - SQUARE_SIZE - 70,
                                 self.x_clicked[i][1] * SQUARE_SIZE + HEIGHT / 2 - SQUARE_SIZE - 70
                             ),
                             (
                                 self.x_clicked[i][0] * SQUARE_SIZE + WIDTH / 2 - SQUARE_SIZE + 70,
                                 self.x_clicked[i][1] * SQUARE_SIZE + HEIGHT / 2 - SQUARE_SIZE + 70
                             ),
                             width=20
                             )
            pygame.draw.line(screen, 'black',
                             (
                                 self.x_clicked[i][0] * SQUARE_SIZE + WIDTH / 2 - SQUARE_SIZE + 70,
                                 self.x_clicked[i][1] * SQUARE_SIZE + HEIGHT / 2 - SQUARE_SIZE - 70
                             ),
                             (
                                 self.x_clicked[i][0] * SQUARE_SIZE + WIDTH / 2 - SQUARE_SIZE - 70,
                                 self.x_clicked[i][1] * SQUARE_SIZE + HEIGHT / 2 - SQUARE_SIZE + 70
                             ),
                             width=20
                             )

    #draw initial board
    def draw_initial(self, screen):
        rect = (0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(screen, 'white', rect)

        for i in range(-1, 2):
            color = 'black'
            rect = (
                WIDTH / 2 - SQUARE_SIZE / 2 - i * SQUARE_SIZE, HEIGHT / 2 - SQUARE_SIZE / 2 - 1 * SQUARE_SIZE,
                SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect, width=1)
            rect = (
                WIDTH / 2 - SQUARE_SIZE / 2 - i * SQUARE_SIZE, HEIGHT / 2 - SQUARE_SIZE / 2 - 0 * SQUARE_SIZE,
                SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect, width=1)
            rect = (
                WIDTH / 2 - SQUARE_SIZE / 2 - i * SQUARE_SIZE, HEIGHT / 2 - SQUARE_SIZE / 2 + 1 * SQUARE_SIZE,
                SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect, width=1)

    def draw_game_over(self, screen):
        if self.game_over():
            font = pygame.font.Font('freesansbold.ttf', 32)
            if self.game_state() == 'draw':
                text = font.render(self.game_state(), True, 'white')
            else:
                text = font.render(self.game_state() + ' win', True, 'white')
            color = 'blue'
            rect = (WIDTH // 2 - 150, HEIGHT // 2 - 75, 300, 150)
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, (WIDTH // 2 - 75 // 2, HEIGHT // 2 - 32.5 // 2))

    def reset(self):
        self.__init__()

    def update_board(self):
        for i in range(len(self.o_clicked)):
            self.board[int(self.o_clicked[i][0])][int(self.o_clicked[i][1])] = 'o'
        for i in range(len(self.x_clicked)):
            self.board[int(self.x_clicked[i][0])][int(self.x_clicked[i][1])] = 'x'

    def get_board(self):
        return self.board

    def possible_moves(self):
        possible_moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '_':
                    possible_moves.append((i, j))
        return possible_moves

    def undo_move(self, move):
        if move in self.o_clicked:
            self.o_clicked.remove(move)
        else:
            self.x_clicked.remove(move)
        self.update_board()

from const import *
from game import Game
import pygame
from ai import AI
from sys import exit
from sys import setrecursionlimit

class Main:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TIC-TAC-TOE")
        self.clock = pygame.time.Clock()


    def mainloop(self):
        game = self.game
        screen = self.screen
        clock = self.clock
        while True:
            game.draw_initial(screen)
            game.draw_(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over():
                    clicked_row, clicked_col = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                    clicked = (clicked_row, clicked_col)
                    game.update(clicked)
                    game.update_board()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        screen = self.screen
                        clock = self.clock
                    if event.key == pygame.K_i:
                        if game.next_player == 1:
                            AI.best_move_for_x(game)
                        else:
                            AI.best_move_for_o(game)

            # setting up the screen
            if game.game_over():
                game.draw_game_over(screen)
            pygame.display.update()
            clock.tick(60)


main = Main()
main.mainloop()

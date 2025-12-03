# main.py

import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.start_game()

    while True:
        game.update()
        game.draw()

if __name__ == "__main__":
    main()
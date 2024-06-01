import sys
import images_path
import pygame
from rummikub_game import RummikubGame


def main():
    game = RummikubGame(pygame.display.set_mode((images_path.WINDOW_WIDTH, images_path.WINDOW_HEIGHT)))
    if "Exit" == game.game_status():
        sys.exit()


if __name__ == "__main__":
    main()

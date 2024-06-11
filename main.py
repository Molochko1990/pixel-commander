import pygame
import sys
from game.settings import *
from game.map_generator import MapGenerator
from game.assets_loader import load_image


def main():
    pygame.init()

    game_icon = load_image('water.png')
    pygame.display.set_icon(game_icon)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pixel Commander')

    # Создаем объект MapGenerator
    map_generator = MapGenerator()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        map_generator.draw_map(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

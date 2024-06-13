import pygame
import sys
from .settings import *
from .map_generator import MapGenerator
from .assets_loader import water_img


class Game:
    def __init__(self):
        pygame.init()

        game_icon = water_img  # заменить на какую-то другую иконку не забыть
        pygame.display.set_icon(game_icon)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pixel Commander')
        self.clock = pygame.time.Clock()
        self.running = True

        self.map_generator = MapGenerator()

        # Тут будет есs

        # и mvc

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # self.controller.handle_input(event)

            # Update ECS systems
            # self.movement_system.update()

            # Update and render MVC
            self.screen.fill(BG_COLOR)
            # self.controller.update(self.entities)
            # self.render_system.render(self.screen)

            self.map_generator.draw_map(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


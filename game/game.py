import pygame
import sys
from .map_generator import MapGenerator
from .mvc.view import View


class Game:
    def __init__(self):
        # создание игрового окна
        self.view = View()
        self.clock = pygame.time.Clock()
        self.running = True

        # создание и управление самой игрой
        self.map_generator = MapGenerator()
        self.game_map = self.map_generator.get_map()


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.view.draw_map(self.game_map)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


import pygame
import sys
from ..model.map_generator import MapGenerator
from ..view.view import View


class Game:
    def __init__(self):
        # создание игрового окна
        self.view = View()
        self.clock = pygame.time.Clock()
        self.running = True
        self.additional_window_open = False

        # создание и управление самой игрой
        self.map_generator = MapGenerator()
        self.game_map = self.map_generator.get_map()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)

    def handle_mouse_click(self, event):
        cell_x, cell_y = self.view.get_cell_under_mouse(event.pos)
        if self.is_city_tile(cell_x, cell_y):
            self.toggle_additional_window()

    def is_city_tile(self, x, y):
        return self.game_map[y][x] in {4, 5}

    def toggle_additional_window(self):
        if self.additional_window_open:
            self.additional_window_open = False
        else:
            self.additional_window_open = True

    def draw_ui(self):
        self.view.draw_map(self.game_map)
        if self.additional_window_open:
            self.view.draw_unit_order_window()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw_ui()
            # self.view.draw_map(self.game_map)
            # self.view.draw_unit_order_window()
            #
            # pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


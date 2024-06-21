import pygame
import sys
from ..model.map_generator import MapGenerator
from ..view.view import View
from ..model.game_state import GameState


class Game:
    def __init__(self):
        # создание игрового окна
        self.view = View()
        self.clock = pygame.time.Clock()
        self.running = True
        self.additional_window_open = False

        # создание и управление самой игрой
        self.game_state = GameState()
        self.map_generator = MapGenerator()
        self.game_map = self.map_generator.get_map()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_turn()

    def next_turn(self):
        self.game_state.next_turn()

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
            self.view.draw_unit_order_window(self.order_unit)

        pygame.display.flip()

    def order_unit(self, unit_type):
        player_id = self.game_state.get_current_player()
        production_time = {"Солдат": 0, "Танк": 2}.get(unit_type)
        self.game_state.add_unit_to_production_queue(player_id, unit_type, production_time)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw_ui()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


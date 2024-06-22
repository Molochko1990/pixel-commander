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
        self.game_state.add_cities(self.game_map)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_turn()

    def handle_mouse_click(self, event):
        mouse_pos = event.pos
        if self.additional_window_open:
            for button in self.view.order_buttons:
                if button['rect'].collidepoint(mouse_pos):
                    button['callback']()
        else:
            for button in self.view.interface_buttons:
                if button['rect'].collidepoint(mouse_pos):
                    button['callback']()
    def next_turn(self):
        self.game_state.next_turn()

    def is_city_tile(self, x, y):
        return self.game_map[y][x] in {4, 5}

    def toggle_additional_window(self):
        self.additional_window_open = not self.additional_window_open

    def draw_ui(self):
        self.view.draw_map(self.game_map)
        self.view.draw_interface(self.game_state.next_turn, self.toggle_additional_window)
        if self.additional_window_open:
            self.view.draw_unit_order_window(self.order_unit, self.toggle_additional_window)
        self.view.draw_units(self.game_state.cities)
        self.view.draw_units(self.game_state.entities)
        pygame.display.flip()

    def order_unit(self, unit_type):
        player_id = self.game_state.get_current_player()
        production_time = {"Солдат": 0, "Танк": 2}.get(unit_type)
        self.game_state.add_unit_to_production_queue(player_id, unit_type, production_time)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw_ui()
            self.game_state.process_production_queue()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


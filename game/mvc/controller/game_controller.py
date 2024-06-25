import pygame
import sys
from ..model.map_generator import MapGenerator
from ..view.view import View
from ..model.game_state import GameState
from ...ecs.entities.entities import SoldierEntity, TankEntity
from ...settings import TILE_SIZE
from ...assets_loader import load_images


class Game:
    def __init__(self) -> None:
        self.view = View()
        self.clock = pygame.time.Clock()
        self.running = True
        self.additional_window_open = False

        self.game_state = GameState()
        self.map_generator = MapGenerator()
        self.game_map = self.map_generator.get_map()
        self.game_state.add_cities(self.map_generator.generate_city_spawn)

        self.selected_marker_image = load_images().get(10)


    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_turn()

    def handle_mouse_click(self, event) -> None:
        mouse_pos = event.pos
        if self.additional_window_open:
            for button in self.view.order_buttons:
                if button['rect'].collidepoint(mouse_pos):
                    button['callback']()
        else:
            for button in self.view.interface_buttons:
                if button['rect'].collidepoint(mouse_pos):
                    button['callback']()

            self.check_unit_selection(mouse_pos)

    def check_unit_selection(self, mouse_pos) -> None:
        tile_x, tile_y = mouse_pos[0] // TILE_SIZE, mouse_pos[1] // TILE_SIZE
        for player_id, unit_list in self.game_state.entities.items():
            for unit in unit_list:
                pos = unit.get_component('position')
                if pos.x == tile_x and pos.y == tile_y:
                    self.game_state.select_unit(unit)
                    return
        self.game_state.deselect_unit()

    def next_turn(self) -> None:
        self.game_state.next_turn()

    def toggle_additional_window(self) -> None:
        self.additional_window_open = not self.additional_window_open

    def draw_ui(self) -> None:
        self.view.draw_map(self.game_map)
        self.view.draw_interface(self.next_turn, self.toggle_additional_window, self.game_state.get_current_player(), self.game_state.get_current_turn())
        self.view.draw_units(self.game_state.cities)
        self.view.draw_units(self.game_state.entities)
        self.view.draw_selected_unit_marker(self.game_state.get_selected_unit(), self.selected_marker_image)
        if self.additional_window_open:
            self.view.draw_unit_order_window(self.order_unit, self.toggle_additional_window)
        pygame.display.flip()

    def order_unit(self, unit_type: SoldierEntity | TankEntity) -> None:
        player_id = self.game_state.get_current_player()
        production_turns_for_unit = {SoldierEntity: 1, TankEntity: 2}.get(unit_type)
        self.game_state.add_unit_to_production_queue(player_id, unit_type, production_turns_for_unit)

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.draw_ui()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


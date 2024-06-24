import pygame

from ...ecs.entities.entities import SoldierEntity, TankEntity, CityEntity
from ...assets_loader import load_images
from ...settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from ...settings import TILE_SIZE


class View:
    def __init__(self) -> None:
        pygame.init()
        game_icon = next(iter(load_images().values()))  # заменить на какую-то другую иконку не забыть
        pygame.display.set_icon(game_icon)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('Pixel Commander')

        self.IMAGES: dict[int, any] = load_images()  # any это же относится к png картинкам ?
        self.interface_buttons: list[dict[str: any]] = []
        self.order_buttons: list[dict[str: any]] = []

    def draw_map(self, game_map: list[list[int]]):
        self.screen.fill(BG_COLOR)
        for row in range(len(game_map)):
            for col in range(len(game_map[0])):
                tile_value = game_map[row][col]
                tile_image = self.IMAGES[tile_value]
                self.screen.blit(tile_image, (col * TILE_SIZE, row * TILE_SIZE))

    def draw_interface(self, next_turn: callable, toggle_additional_window: callable):
        mouse_pos = self.get_mouse_pos()

        button_color = (255, 200, 100)
        button_hover_color = (200, 200, 200)

        self.interface_buttons = [
            {"rect": pygame.Rect(1690, 1000, 220, 50), "color": button_color, "hover_color": button_hover_color,
             "text": "Следующий Ход", "callback": lambda: next_turn()},
            {"rect": pygame.Rect(10, 1000, 180, 50), "color": button_color, "hover_color": button_hover_color,
             "text": "Заказ Юнитов", "callback": lambda: toggle_additional_window()},
        ]

        for button in self.interface_buttons:
            if button['rect'].collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, button["hover_color"], button["rect"])
            else:
                pygame.draw.rect(self.screen, button["color"], button["rect"])

            font = pygame.font.Font(None, 36)
            text = font.render(button["text"], True, (0, 0, 0))
            text_rect = text.get_rect(center=button["rect"].center)
            self.screen.blit(text, text_rect)

    def draw_unit_order_window(self, order_unit: callable, toggle_additional_window: callable):
        ui_width = 200
        ui_height = SCREEN_HEIGHT
        ui_panel = pygame.Surface((ui_width, ui_height))
        ui_panel.fill((50, 50, 50))
        button_color = (100, 200, 100)
        button_hover_color = (200, 200, 200)

        self.order_buttons = [
            {"rect": pygame.Rect(10, 30, 180, 50), "color": button_color, "hover_color": button_hover_color,
             "text": "Солдат",
             "callback": lambda: order_unit(SoldierEntity)},
            {"rect": pygame.Rect(10, 100, 180, 50), "color": button_color, "hover_color": button_hover_color,
             "text": "Танк",
             "callback": lambda: order_unit(TankEntity)},
            {"rect": pygame.Rect(10, 990, 180, 50), "color": button_color, "hover_color": button_hover_color,
             "text": "Закрыть",
             "callback": lambda: toggle_additional_window()}
        ]

        mouse_pos = pygame.mouse.get_pos()

        for button in self.order_buttons:
            if button['rect'].collidepoint(mouse_pos):
                pygame.draw.rect(ui_panel, button["hover_color"], button["rect"])
            else:
                pygame.draw.rect(ui_panel, button["color"], button["rect"])

            font = pygame.font.Font(None, 36)
            text_surf = font.render(button["text"], True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=button["rect"].center)
            ui_panel.blit(text_surf, text_rect)

        self.screen.blit(ui_panel, (0, 0))

    def draw_units(self, unit_entities: dict[int, SoldierEntity | TankEntity | CityEntity]): # сюда могут помещаться разные классы например SoldierEntity, TankEntity
        for unit in unit_entities.values():
            position = unit.get_component('position')
            render = unit.get_component('render')
            self.screen.blit(render.image, (position.x * TILE_SIZE, position.y * TILE_SIZE))

    @staticmethod
    def get_mouse_pos() -> tuple[int, int]:
        return pygame.mouse.get_pos()

    # возможно можно удалить уже эту функцию
    def get_cell_under_mouse(self, pos):
        mouse_x, mouse_y = pos
        cell_x = mouse_x // TILE_SIZE
        cell_y = mouse_y // TILE_SIZE
        return cell_x, cell_y

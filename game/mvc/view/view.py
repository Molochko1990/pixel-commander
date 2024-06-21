import pygame

from ...assets_loader import load_images
from ...settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from ...settings import TILE_SIZE

class View:
    def __init__(self):
        pygame.init()
        game_icon = next(iter(load_images().values()))  # заменить на какую-то другую иконку не забыть
        pygame.display.set_icon(game_icon)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('Pixel Commander')
        self.IMAGES = load_images()

    def draw_map(self, game_map):
        self.screen.fill(BG_COLOR)
        for row in range(len(game_map)):
            for col in range(len(game_map[0])):
                tile_value = game_map[row][col]
                tile_image = self.IMAGES[tile_value]
                self.screen.blit(tile_image, (col * TILE_SIZE, row * TILE_SIZE))

    def draw_unit_order_window(self, order_unit_callback):
        ui_width = 200
        ui_height = SCREEN_HEIGHT
        ui_panel = pygame.Surface((ui_width, ui_height))
        ui_panel.fill((50, 50, 50))
        buttons = [
            {"rect": pygame.Rect(10, 10, 180, 50), "color": (100, 200, 100), "text": "Солдат",
             "callback": lambda: order_unit_callback("Солдат")},
            {"rect": pygame.Rect(10, 70, 180, 50), "color": (100, 200, 100), "text": "Танк",
             "callback": lambda: order_unit_callback("Танк")}
        ]

        for button in buttons:
            pygame.draw.rect(ui_panel, button["color"], button["rect"])
            font = pygame.font.Font(None, 36)
            text_surf = font.render(button["text"], True, (255, 255, 255))
            ui_panel.blit(text_surf, (button["rect"].x + 5, button["rect"].y + 10))

        self.screen.blit(ui_panel, (SCREEN_WIDTH - ui_width, 0))

    def get_cell_under_mouse(self, pos):
        mouse_x, mouse_y = pos
        cell_x = mouse_x // TILE_SIZE
        cell_y = mouse_y // TILE_SIZE
        return cell_x, cell_y

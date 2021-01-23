import pygame

from arcanoid.third_party.button import Button
from arcanoid.constants import BLUE, GREEN, BLACK, ORANGE
from arcanoid.objects.base import DrawableObject


class ButtonObject(DrawableObject):
    BUTTON_STYLE = {
        "hover_color": BLUE,
        "clicked_color": GREEN,
        "clicked_font_color": BLACK,
        "hover_font_color": ORANGE,
    }

    def __init__(self, game, x, y, width, height, color, function, text):
        super().__init__(game)
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.button = Button((x, y, width, height), color, function, text=text, **self.BUTTON_STYLE)

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self):
        self.button.update(self.game.screen)

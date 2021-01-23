import pygame
from arcanoid.constants import BLACK


class DrawableObject:
    def __init__(self, game):
        self.game = game
        self.color = BLACK
        self.rect = pygame.rect.Rect(0, 0, 0, 0)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_center(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def process_event(self, event):
        pass

    def process_logic(self):
        pass

    def process_draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 3)

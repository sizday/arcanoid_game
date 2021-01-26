import pygame
import random
from arcanoid.objects.image import ImageObject


class BallObject(ImageObject):
    filename = 'images/basketball.png'
    image = pygame.image.load(filename)
    max_speed = 2

    def __init__(self, game, x=None, y=None, speed=None):
        super().__init__(game)
        self.rect.x = x if x else game.width // 2
        self.rect.y = y if y else game.height // 2
        self.radius = self.rect.width // 2
        self.speed = speed if speed else [self.get_random_speed(), self.get_random_speed()]
        self.shift = [0.5 for _ in range(2)]

    @staticmethod
    def get_random_speed():
        return random.choice([1, -1]) * (random.random() + 1)

    def collides_with_platform(self, platform):
        return pygame.sprite.collide_rect(self, platform)

    def collides_with_border(self, border):
        return pygame.sprite.collide_rect(self, border)

    def bounce(self):
        self.speed[1] = -1 * self.speed[1]
        for i in range(2):
            if self.speed[i] < 0:
                self.speed[i] -= self.shift[i]
            else:
                self.speed[i] += self.shift[i]

    def vertical_edge_collision(self):
        return self.rect.right >= self.game.width or self.rect.left <= 0

    def horizontal_edge_collision(self):
        return self.rect.bottom >= self.game.height or self.rect.top <= 0

    def edge_collision(self):
        return self.horizontal_edge_collision() or self.vertical_edge_collision()

    def check_borders(self):
        if self.vertical_edge_collision():
            self.speed[0] *= -1
        if self.horizontal_edge_collision():
            self.speed[1] *= -1

    def step(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def process_logic(self):
        self.check_borders()
        self.step()

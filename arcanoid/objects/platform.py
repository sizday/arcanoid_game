from arcanoid.objects.base import DrawableObject
from arcanoid.constants import BLUE


class PlatformObject(DrawableObject):
    def __init__(self, game, speed=3):
        super().__init__(game)
        self.rect.x = 20
        self.rect.y = game.height - 40
        self.rect.width = 200
        self.rect.height = 30
        self.max_speed = speed
        self.color = BLUE
        self.speed_y = 0

    def left_edge_collision(self):
        return self.rect.left <= 0

    def right_edge_collision(self):
        return self.rect.right >= self.game.width

    def check_borders(self):
        if self.left_edge_collision():
            self.speed_y = 0
            self.rect.x = 1
        if self.right_edge_collision():
            self.speed_y = 0
            self.rect.x = self.game.width - self.rect.width - 1

    def step(self):
        self.rect.x += self.speed_y

    def process_logic(self):
        self.check_borders()
        self.step()

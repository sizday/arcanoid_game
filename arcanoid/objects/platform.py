from arcanoid.objects.base import DrawableObject
from arcanoid.constants import BLACK


class PlatformObject(DrawableObject):
    def __init__(self, game, x=0, y=0, width=1, height=1, color=BLACK, speed=3):
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.max_speed = speed
        self.color = color
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

from arcanoid.objects.base import DrawableObject


class BottomBorderObject(DrawableObject):
    def __init__(self, game, speed=3):
        super().__init__(game)
        self.rect.x = 0
        self.rect.y = game.height - 1
        self.rect.width = game.width
        self.rect.height = 1
        self.max_speed = speed
        self.speed_y = 0

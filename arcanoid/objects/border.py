from arcanoid.objects.base import DrawableObject


class BorderObject(DrawableObject):
    def __init__(self, game, x=0, y=0, width=1, height=1):
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

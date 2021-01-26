from arcanoid.constants import RED
from arcanoid.objects.button import ButtonObject
from arcanoid.scenes.base import BaseScene


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 - 20 - 25, 200, 50,
                RED, self.start_game, text='Запуск игры'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 + 25, 200, 50,
                RED, self.game.exit_game, text='Выход'
            )
        )

    def start_game(self):
        self.game.scores[0] = 0
        self.game.scores[1] = 0
        self.game.set_scene(self.game.SCENE_GAME)

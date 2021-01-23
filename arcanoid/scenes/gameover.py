from datetime import datetime

from arcanoid.objects.text import TextObject
from arcanoid.scenes.base import BaseScene


class GameOverScene(BaseScene):
    text_format = 'Game over ({})'
    seconds_to_end = 5

    def __init__(self, game):
        super().__init__(game)
        self.time_start = datetime.now()
        self.last_seconds_passed = 0
        self.text = TextObject(self.game, self.game.width // 2, self.game.height // 2,
                               self.get_game_over_text_formatted(), (255, 255, 255))
        self.objects.append(self.text)
        self.update_start_time()

    def get_game_over_text_formatted(self):
        return self.text_format.format(self.seconds_to_end - self.last_seconds_passed)

    def on_activate(self):
        self.objects = [self.text]
        self.update_start_time()
        self.update_scores()

    def update_scores(self):
        self.scores = sorted([int(score[:-1]) for score in open("high_scores.txt").readlines()], reverse=True)
        self.text_scores = [TextObject(self.game, self.game.width // 2, i * 30 + 50,
                                       f'{i+1}: {self.scores[i]}', (255, 255, 255)) for i in range(len(self.scores))]
        for text_score in self.text_scores:
            self.objects.append(text_score)

    def update_start_time(self):
        self.time_start = datetime.now()

    def process_logic(self):
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.last_seconds_passed = seconds_passed
            self.objects[0].update_text(self.get_game_over_text_formatted())
        if seconds_passed >= self.seconds_to_end:
            self.game.set_scene(self.game.SCENE_MENU)

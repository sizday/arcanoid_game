import pygame
import time
from arcanoid.objects.ball import BallObject
from arcanoid.objects.platform import PlatformObject
from arcanoid.objects.bottom_border import BottomBorderObject
from arcanoid.objects.text import TextObject
from arcanoid.scenes.base import BaseScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.ball = BallObject(game)
        self.platform = PlatformObject(game)
        self.bottom_border = BottomBorderObject(game)
        self.timer = time.time()
        self.timer_text = TextObject(self.game, 0, 0, self.get_timer_text(), (255, 255, 255))
        self.timer_text.move(50, 50)
        self.objects.append(self.ball)
        self.objects.append(self.platform)
        self.objects.append(self.bottom_border)
        self.objects.append(self.timer_text)

    def on_activate(self):
        self.timer = time.time()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)
            if event.key == pygame.K_a:
                self.platform.speed_y = -1 * self.platform.max_speed
            if event.key == pygame.K_d:
                self.platform.speed_y = self.platform.max_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                self.platform.speed_y = 0

    def check_ball_inter_collisions(self):
        if self.ball.collides_with_platform(self.platform):
            self.ball.bounce()
        if self.ball.collides_with_bottom_border(self.bottom_border):
            high_scores_file = open("high_scores.txt", "a")
            high_scores_file.write(str(int(time.time() - self.timer))+"\n")
            high_scores_file.close()
            self.game.set_scene(self.game.SCENE_GAME_OVER)

    def get_timer_text(self):
        return f'Points: {int(time.time() - self.timer)}'

    def set_timer(self):
        self.timer_text.update_text(self.get_timer_text())
        self.timer_text.move(10, 10)

    def process_logic(self):
        super().process_logic()
        self.set_timer()
        self.check_ball_inter_collisions()

import pygame
from arcanoid.objects.ball import BallObject
from arcanoid.objects.platform import PlatformObject
from arcanoid.objects.border import BorderObject
from arcanoid.objects.text import TextObject
from arcanoid.scenes.base import BaseScene
from arcanoid.constants import BLUE, RED


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.ball = BallObject(game)
        self.bottom_platform = PlatformObject(game, x=20, y=game.height-40, width=200, height=30, color=BLUE)
        self.top_platform = PlatformObject(game, x=20, y=10, width=200, height=30, color=RED)
        self.bottom_border = BorderObject(game, x=0, y=game.height-1, width=game.width, height=1)
        self.top_border = BorderObject(game, x=0, y=0, width=game.width, height=1)
        self.score_text = TextObject(self.game, 0, 0, self.get_score(), (255, 255, 255))
        self.score_text.move(20, game.height//2)
        self.objects = [self.top_platform, self.bottom_platform, self.top_border, self.bottom_border, self.score_text]
        self.objects.append(self.ball)

    def on_activate(self):
        self.objects.pop()
        self.ball = BallObject(self.game)
        self.objects.append(self.ball)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)
            if event.key == pygame.K_a:
                self.bottom_platform.speed_y = -1 * self.bottom_platform.max_speed
            if event.key == pygame.K_d:
                self.bottom_platform.speed_y = self.bottom_platform.max_speed
            if event.key == pygame.K_LEFT:
                self.top_platform.speed_y = -1 * self.bottom_platform.max_speed
            if event.key == pygame.K_RIGHT:
                self.top_platform.speed_y = self.bottom_platform.max_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                self.bottom_platform.speed_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.top_platform.speed_y = 0

    def check_ball_inter_collisions(self):
        if self.ball.collides_with_platform(self.bottom_platform) or \
                self.ball.collides_with_platform(self.top_platform):
            self.ball.bounce()
        if self.ball.collides_with_border(self.top_border):
            self.game.scores[0] += 1
            self.game.set_scene(self.game.SCENE_GAME)
        if self.ball.collides_with_border(self.bottom_border):
            self.game.scores[1] += 1
            self.game.set_scene(self.game.SCENE_GAME)
        if self.game.scores[0] == 3 or self.game.scores[1] == 3:
            open("high_scores.txt", "a").write(str(self.get_score())+"\n")
            self.game.set_scene(self.game.SCENE_GAME_OVER)

    def get_score(self):
        return f'{self.game.scores[0]}:{self.game.scores[1]}'
        
    def set_text(self):
        self.score_text.update_text(self.get_score())
        self.score_text.move(20, self.game.height//2)

    def process_logic(self):
        super().process_logic()
        self.set_text()
        self.check_ball_inter_collisions()

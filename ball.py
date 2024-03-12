import pygame,constants
from gameobject import GameObject


class Ball(GameObject):
    def __init__(self, paddle):
        super().__init__(constants.RED, 10, 10, (constants.SCREEN_WIDTH - 10) // 2, 
                         constants.SCREEN_HEIGHT - 70)
        self.paddle = paddle
        self.speed_x = 3
        self.speed_y = -3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= constants.SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y
        if pygame.sprite.collide_rect(self, self.paddle):
            self.speed_y = -self.speed_y
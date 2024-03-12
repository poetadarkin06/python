import constants
from gameobject import GameObject


class Paddle(GameObject):
    def __init__(self):
        super().__init__(constants.BLUE, 100, 10, (constants.SCREEN_WIDTH - 100) // 2, 
                         constants.SCREEN_HEIGHT - 50)
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH

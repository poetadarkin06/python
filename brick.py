import constants
from gameobject import GameObject

class Brick(GameObject):
    def __init__(self, x, y):
        super().__init__(constants.GREEN, constants.BRICK_WIDTH, constants.BRICK_HEIGHT, x, y)
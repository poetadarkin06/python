import pygame , constants , sys
from paddle import Paddle
from brick import Brick
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.all_sprites.add(self.paddle, self.ball)
        self.lives = 3
        self.score = 0
        self.generate_bricks()

    def generate_bricks(self):
        for row in range(4):
            for column in range(10):
                brick = Brick(column * (constants.BRICK_WIDTH + constants.BRICK_GAP), 
                              row * (constants.BRICK_HEIGHT + constants.BRICK_GAP) + 50)
                self.bricks.add(brick)
                self.all_sprites.add(brick)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.paddle.speed = -5
                elif event.key == pygame.K_RIGHT:
                    self.paddle.speed = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.paddle.speed = 0

    def update(self):
        self.all_sprites.update()
        brick_collisions = pygame.sprite.spritecollide(self.ball, self.bricks, True)
        if brick_collisions:
            self.ball.speed_y = -self.ball.speed_y
            self.score += 1
        if self.ball.rect.bottom >= constants.SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives > 0:
                self.ball.rect.x = self.paddle.rect.x + self.paddle.rect.width // 2 - self.ball.rect.width // 2
                self.ball.rect.y = self.paddle.rect.y - self.ball.rect.height
                self.ball.speed_y = -3
            else:
                self.game_over()

    def draw(self):
        self.screen.fill(constants.BLACK)
        self.all_sprites.draw(self.screen)
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {self.lives}", True, constants.WHITE)
        score_text = font.render(f"Score: {self.score}", True, constants.WHITE)
        self.screen.blit(lives_text, (10, 10))
        self.screen.blit(score_text, (constants.SCREEN_WIDTH - 150, 10))
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, constants.RED)
        restart_text = font.render("Press R to restart", True, constants.WHITE)
        self.screen.blit(game_over_text, (constants.SCREEN_WIDTH // 2 - 200, constants.SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(restart_text, (constants.SCREEN_WIDTH // 2 - 250, constants.SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
        self.reset()

    def reset(self):
        self.all_sprites.empty()
        self.bricks.empty()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.all_sprites.add(self.paddle, self.ball)
        self.lives = 3
        self.score = 0
        self.generate_bricks()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)




if __name__ == "__main__":
    game = Game()
    game.run()
           
           
           
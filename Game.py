######################################################################
# Author: CJ Spencer, Dawson Lakes      TODO: Change this to your names
# Username: spencerc, lakesd3            TODO: Change this to your usernames
#
# Assignment: Final Project
#
# Purpose: Make a cool game
######################################################################
# Acknowledgements:
####################################################################################

import pygame
from Fruits import Fruits, Fruit1, Fruit2
from Player import Player



class Game:
    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.background_image = pygame.image.load("images/tree.png")
        self.background_image = pygame.transform.scale(self.background_image, self.size)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.player = Player(self.size)
        self.fruit = Fruits
        self.apple = Fruit1(self.size)
        self.green_apple = Fruit2(self.size)
        self.score = 0
        self.lives = 3

    def game_over(self):
        """
        Displays the game-over screen.
        """
        game_over_font = pygame.font.Font(None, 80)
        game_over_text = game_over_font.render("Game Over!", True, (255, 0, 0))
        restart_text = pygame.font.Font(None, 36).render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        while self.game_over_flag:
            self.screen.fill((0, 0, 0))
            self.screen.blit(game_over_text, (self.size[0] // 2 - game_over_text.get_width() // 2, self.size[1] // 3))
            self.screen.blit(restart_text, (self.size[0] // 2 - restart_text.get_width() // 2, self.size[1] // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over_flag = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()  # Restart the game
                        self.run()
                    elif event.key == pygame.K_q:
                        self.game_over_flag = False
                        self.running = False

    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Check for apple going below screen border
            if self.apple.rect.bottom >= self.size[1] or self.green_apple.rect.bottom >= self.size[1]:
                self.running = False
                self.game_over_flag = True  # Trigger game-over screen
            if self.green_apple.rect.bottom >= self.size[1]:
                self.green_apple.reset()
                self.lives -= 1
                if self.lives == 0:
                    self.running = False  # End game
            if self.apple.rect.bottom >= self.size[1]:
                self.apple.reset()
                self.lives -= 1
                if self.lives == 0:
                    self.running = False  # End game


            if pygame.sprite.collide_rect(self.player, self.apple):
                self.score += 1
                self.apple.reset()
            if pygame.sprite.collide_rect(self.player, self.green_apple):
                self.score += 1
                self.green_apple.reset()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.player.movement(pygame.key.get_pressed())
                self.apple.movement()
                self.green_apple.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.player.surf, self.player.rect)
                self.screen.blit(self.apple.surf, self.apple.rect)
                self.screen.blit(self.green_apple.surf, self.green_apple.rect)
                font = pygame.font.Font(None, 36)
                score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
                self.screen.blit(score_text, (10, 10))
                lives_text = font.render(f"Lives: {self.lives}", True, (0, 0, 0))
                self.screen.blit(lives_text, (700, 10))

            if not self.running:
                game_over_text = game_over_font.render("Game Over!", True, (255, 0, 0))
                self.screen.blit(game_over_text,(self.size[0] // 2 - game_over_text.get_width() // 2, self.size[1] // 3))

            pygame.display.update()
            self.clock.tick(24)

        if self.game_over_flag:
            self.game_over()

        pygame.quit()


def main():
    """
    Starts the cat game.

    :return: None
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

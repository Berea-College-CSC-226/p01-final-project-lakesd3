######################################################################
# Author: CJ Spencer, Dawson Lakes
# Username: spencerc, lakesd3
#
# Assignment: Final Project
#
# Purpose: Make a cool game
######################################################################
# Acknowledgements:
####################################################################################
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning player")
        self.surf = pygame.image.load('images/player.gif').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (75, 75))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)
        self.rect.bottom = self.screen_size[1]
        self.rect.centerx = self.screen_size[0] // 2


    def movement(self, keys):
        """
        Handles left and right movement events from the user

        :param keys: key presses from pygame event listener

        :return: None
        """
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(45, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-45, 0)



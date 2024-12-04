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
import pygame, random
import time


class Fruits(pygame.sprite.Sprite):
    move_distance = 10
    directions = ["south"]

    def __init__(self, screen_size, image_path):
        """
        Represents the falling red apple in the game.

        :param screen_size: size of the window, for ensuring the NPC stays on screen
        """
        self.screen_size = screen_size
        super().__init__()
        print(f"Spawning {self.__class__.__name__}")  # Print specific object name
        self.surf = pygame.image.load(image_path)
        self.surf = pygame.transform.scale(self.surf, (25, 25))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//4, self.screen_size[1]//4)
        self.path = random.choice(self.directions)
        self.rect.top = 0
        self.rect.x = random.randint(150, self.screen_size[0] - self.rect.width)
        self.path = random.choice(self.directions)
        self.position = [0,0]

    def get_direction(self):
        """
        Makes the apple fall

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "south"

    def movement(self):
        """
        Moves the NPC around.

        :return: None
        """

        if self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance

        self.get_direction()

class Fruit1(Fruits):
    """
    Represents a falling apple in the game.

    Inherits from the Fruits class.
    """
    def __init__(self, screen_size):
        """
        Initializes a falling apple.
        """
        super().__init__(screen_size, "images/apple.png")

    def get_direction(self):
        """
        Makes the apple fall

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "south"

    def reset(self):
        # Set apple to top of the screen with random x position
        self.rect.top = 0
        self.rect.x = random.randint(0, self.screen_size[0] - self.rect.width)

    def movement(self):
        """
        Moves the NPC around.

        :return: None
        """

        if self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance

        self.get_direction()

class Fruit2(Fruits):
    """
    Represents a falling green_apple in the game.

    Inherits from the Fruits class.
    """
    def __init__(self, screen_size):
        """
        Initializes a falling apple.
        """
        super().__init__(screen_size, "images/granny_smith.png")
        self.start_time = None



    def reset(self):
        # Set apple to top of the screen with random x position
        self.rect.top = 0
        self.rect.x = random.randint(0, self.screen_size[0] - self.rect.width)

    def movement(self):
        """
        Moves the NPC around.

        :return: None
        """
        if self.start_time is None:
            self.start_time = time.time()  # Start timer on first call

        current_time = time.time()
        if current_time - self.start_time >= 2:  # Check if 2 seconds have passed
            if self.path == "south":
                self.rect.move_ip(0, self.move_distance)

        self.get_direction()
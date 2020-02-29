import pygame


class  Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        # display default: 1300px wide and 700px high
        self.screen_width = 1300
        self.screen_height = 700
        # Set the background color
        self.bg_color = (230, 230, 230)

        # Set the background image
        # self.screen = ai_game.screen
        # self.image = pygame.image.load('images/stars.bmp')

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        # change the bullet speed for faster bullets default: 2.0
        self.bullet_speed = 5.5
        # change the bullet width for multiple hits and spreadshot default: 3
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        # Number of bullets allowed to be on screen at one time
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        # change drop speed for the aliens (test purposes) default: 10
        self.fleet_drop_speed = 100
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
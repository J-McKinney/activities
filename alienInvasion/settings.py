import pygame


class  Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
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
        # ship speed default: 1.5
        self.ship_speed = 1.5
        # ship lives default: 3
        self.ship_limit = 3

        # Bullet settings
        # change the bullet speed for faster bullets default: 2.0
        self.bullet_speed = 2.0
        # change the bullet width for multiple hits and spreadshot default: 3
        self.bullet_width = 3
        # bullet height default: 15
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        # Number of bullets allowed to be on screen at one time default: 4
        self.bullets_allowed = 4

        # Alien settings
        # alien sidescroll speed default: 1.0
        self.alien_speed = 1.0
        # change drop speed for the aliens (test purposes) default: 10
        self.fleet_drop_speed = 10

        # How quickly the game speeds up default: 1.1
        self.speedup_scale = 1.1

        # How quickly the points add up default: 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        # dynamic ship speed up per level default: 1.5
        self.ship_speed = 1.5
        # dynamic bullet speed up per level default: 3.0
        self.bullet_speed = 3.0
        # dynamic alien ship speed up per level default: 1.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring per alien shot down default: 50
        self.alien_points = 50

    
    def increase_speed(self):
        """Increase speed settings and points value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
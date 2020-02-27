class  Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        # display 1300px wide and 700px high
        self.screen_width = 1300
        self.screen_height = 700
        # Set the background color
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        # Number of bullets allowed to be on screen at one time
        self.bullets_allowed = 3
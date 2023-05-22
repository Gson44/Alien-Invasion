class Settings():
    """A class to store all setting for Aliean Invasion."""
    
    def __init__(self):
        """Initialize the game's setting."""
        #Screen settings
        self.screen_width = 1750
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        
        #Ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 50
        self.bullet_color = 200,60,60
        self.bullets_allowed = 3
        
        #Alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 50
        
        #How quickly the game speed up
        self.speedup_scale = 1.1
        
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        
        #Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughtout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_facotr = 1
        
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        #Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_point = int(self.alien_points * self.score_scale)
        print(self.alien_points)
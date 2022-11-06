class Settings:

    """初始化游戏设置"""

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 1.5
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1代表右移,2代表左移
        self.fleet_direction = 1
        # 1代表向右移动,2代表向左移动
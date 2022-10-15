
import sys

import pygame

from settings import Settings 
from ship import Ship

class AlienInvasion:
    """管理游戏资源"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # 设置背景颜色
        #self.bg_color = {230,230,230}

    def run_game(self):
        while True:
        # 监视键盘和鼠标事件
            self._chek_events()

            self.ship.update()
        # 重绘屏幕
            self._update_screen()

            
    
    def _chek_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.type == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.type == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()




if __name__ == '__main__':

    ai = AlienInvasion()
    
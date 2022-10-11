
import sys

import pygame

from settings import Settings 

class AlienInvasion:
    """管理游戏资源"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 设置背景颜色
        #self.bg_color = {230,230,230}

    def run_game(self):
        while True:
        # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':

    ai = AlienInvasion()
    
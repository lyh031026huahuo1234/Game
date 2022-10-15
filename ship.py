import pygame

class Ship:
    def __init__(self, ai_game):
        """初始化飞船的位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        """加载飞船图像"""
        self.image = pygame.image.load('images/5.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """绘制图像"""
        self.screen.blit(self.image,self.rect)
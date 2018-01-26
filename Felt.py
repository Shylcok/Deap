# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 14:22
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : Felt.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from imports import *


# ----------------------------------------------------
class Felt(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images\\name.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.speed = 10

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 14:23
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : main.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from imports import *
import Felt as felt

# ----------------------------------------------------
pygame.init()
# 初始化pygame
bg_size = (640, 480)

screen = pygame.display.set_mode(bg_size, RESIZABLE, 32)
# 创建窗口
pygame.display.set_caption("Deep")

background = pygame.image.load('images\\bg.jpg').convert()

clock = pygame.time.Clock()
running = True

me = felt.Felt(bg_size)


# ----------------------------------------------------
def main():
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        key_press = pygame.key.get_pressed()

        if key_press[K_RIGHT] or key_press[K_d]:
            me.moveRight()
        if key_press[K_LEFT] or key_press[K_a]:
            me.moveLeft()

        screen.blit(background, (0, 0))
        screen.blit(me.image, me.rect)

        pygame.display.update()
        clock.tick(60)


# ----------------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except Exception as e:
        print(e)

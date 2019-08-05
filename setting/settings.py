from pygame import *
import pygame.freetype
import random
from math import *

#define

HEIGHT = 400
WIDTH = 300
bv = 5#小球速度
t = 60#每秒执行次数


#init
init()
screen=display.set_mode([WIDTH,HEIGHT],0,32)
display.set_caption("game")
screen.fill((0,0,0))
f1 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 10)

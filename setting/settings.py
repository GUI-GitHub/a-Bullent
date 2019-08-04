from pygame import *
import pygame.freetype
import random
from math import *

#define

HEIGHT=400
WIDTH=320

#init
init()
screen=display.set_mode([WIDTH,HEIGHT],0,32)
display.set_caption("game")
screen.fill((0,0,0))
f1=pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf",10)
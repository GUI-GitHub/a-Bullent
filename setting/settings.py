from pygame import *
import pygame.freetype
import os
import random
from math import *

#define

HEIGHT = 400
WIDTH = 300
bv = 3#小球速度
t = 90#每秒执行次数
pv = 1#道具下落速度

#init
init()
screen = display.set_mode([WIDTH, HEIGHT], 0, 32, OPENGLBLIT)
display.set_caption("game")
print(dir(screen))
screen.fill((0, 0, 0))
f1 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 10)
f2 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 30)
f3 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 50)





sound_path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/bam.wav")
sound_path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/tern.wav")
sound_path3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/los.wav")
sound_path4 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/win.wav")
sound_path5 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/bo.wav")

mixer.init()
bam = mixer.Sound(sound_path1)
tern = mixer.Sound(sound_path2)
los = mixer.Sound(sound_path3)
win = mixer.Sound(sound_path4)
bo = mixer.Sound(sound_path5)



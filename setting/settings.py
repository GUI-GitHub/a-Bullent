from pygame import *
import pygame.freetype
import os
import random
from math import *

#define
from pygame._freetype import Font

HEIGHT = 600
WIDTH = 400
bv = 3#小球速度
t = 90#每秒执行次数
pv = 1#道具下落速度

#init
pygame.mixer.pre_init(44100, 16, 2, 4096)
init()
screen = display.set_mode([WIDTH, HEIGHT], 0, 32, OPENGLBLIT)
screen.fill((255, 255, 255))
screen_rect = screen.get_rect()
display.set_caption("game")

f1 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 10)
f2 = pygame.freetype.Font("C:\\Windows\\Fonts\\mvboli.ttf", 70)
f3 = pygame.freetype.Font("C:\\Windows\\Fonts\\msyh.ttc", 30)

sound_path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/bam.wav")
sound_path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/tern.wav")
sound_path3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/los.wav")
sound_path4 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/win.wav")
sound_path5 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/super.wav")
sound_path6 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/bom.wav")
sound_path7 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/nle.wav")
sound_path8 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/d.wav")
sound_path9 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/bon.wav")

mixer.init()
bam = mixer.Sound(sound_path1)
tern = mixer.Sound(sound_path2)
los = mixer.Sound(sound_path3)
win = mixer.Sound(sound_path4)
super = mixer.Sound(sound_path5)
bom = mixer.Sound(sound_path6)
nle = mixer.Sound(sound_path7)
d = mixer.Sound(sound_path8)
bon = mixer.Sound(sound_path9)

map_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/map")
map_files = []
for dir_path, file, filenames in os.walk(map_path):
    for filename in filenames:
        if filename.endswith(".png"):
            path = os.path.join(dir_path, filename)
            map_files.append(path)
        print("检测到地图", filename[:-4])


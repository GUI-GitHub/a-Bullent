# from pygame import *
# import random
# from math import *
from setting.settings import *
import os
class Ball():
    def __init__(self, speed, pos=(0, 0)):
        image_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"static/d.png")
        self.image = image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = list(speed)

    def move(self, bx, blocks):
        # 碰壁反弹
        if self.rect[0] <= 0 + 1 or self.rect[0] >= WIDTH - self.rect[2] - 1:
            self.speed[0] = -self.speed[0]
        if self.rect[1] <= 0 + 1:
            self.speed[1] = -self.speed[1]

        # 碰板反弹
        if (bx - 30 < self.rect.centerx < bx + 30) and (362 > self.rect[1] > 350 - self.rect[3]):
            self.speed = (math.Vector2(self.rect.centerx, self.rect.centery)-math.Vector2(bx, 340)).normalize()*3
            print(sqrt(self.speed[0] ** 2 + self.speed[1] ** 2))
            print(self.rect.centerx-bx)


        # 碰砖反弹
        for blk in blocks.blocks:
            rblk = (blk.pos[0]+blk.size[0] * 0.5, blk.pos[1] + blk.size[1] * 0.5)

            ballpos = self.rect[0:2]
            rball=(self.rect.centerx, self.rect.centery)
            #  碰右壁                                    碰左壁                                      碰下壁                                碰上壁
            if ballpos[0] < blk.pos[0] + blk.size[0] and ballpos[0] + self.rect[2] > blk.pos[0] and ballpos[1] < blk.pos[1] + blk.size[1] and ballpos[1] + self.rect[3] > blk.pos[1]:
                if ballpos[0] <= blk.pos[0] + blk.size[0] or ballpos[0] + self.rect[2] >= blk.pos[0]:
                    self.speed[1] = -self.speed[1]
                elif ballpos[1] < blk.pos[1] + blk.size[1] or ballpos[1] + self.rect[3] > blk.pos[1]:
                    self.speed[0] = -self.speed[0]


                # if not blk.type==4:
                print(ballpos, blk)
                blk.type = blk.type - 1
                # blocks.blocks.remove(blk)
                break
        # print(self.speed,self.rect)
        self.rect = self.rect.move(self.speed)

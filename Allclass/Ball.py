from setting.settings import *
import os
class Ball():
    def __init__(self, speed, pos=(0, 0)):
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"static/c.png")
        self.image = image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = list(speed)
        self.collide_b = False
        self.collide_wx = False
        self.collide_wy = False

    def move(self, bx, blocks):
        self.rect.x += self.speed[0]




        # 碰壁反弹
        if self.rect.x <= 0 or self.rect.x >= WIDTH - self.rect.w:
            self.speed[0] = -self.speed[0]
        if self.rect.y <= 1:
            self.speed[1] = -self.speed[1]
        if self.rect.y == 0:
            self.speed[1] = bv
        if self.rect.x == 0:
            self.speed[0] = bv
        # 碰方块反弹
        for blk in blocks.blocks:

            rblk = (blk.pos[0]+blk.size[0] * 0.5, blk.pos[1] + blk.size[1] * 0.5)

            ballpos = self.rect[0:2]
            rball=(self.rect.centerx, self.rect.centery)

            if self.rect.x < blk.pos[0] + blk.size[0] and ballpos[0] + self.rect.w > blk.pos[0] and self.rect.y < blk.pos[1] + blk.size[1] and self.rect.y + self.rect.h > blk.pos[1]:
                bam.play()

                if (ballpos[1] <= blk.pos[1] + blk.size[1] or ballpos[1] + self.rect.h >= blk.pos[1]):  # and not self.inb:
                    #碰左右壁
                    self.speed[0] = -self.speed[0]

                if (ballpos[0] <= blk.pos[0] + blk.size[0] or ballpos[0] + self.rect.w >= blk.pos[0])and not self.collide_b:#and not self.inb:
                    #碰上下壁
                    self.speed[1] = -self.speed[1]





                #  if not blk.type==4:
                #print(ballpos, blk)
                if not self.collide_b:
                    blk.count = blk.count - 1
                # blocks.blocks.remove(blk)
                break
                self.collide_b = True
            else:
                self.collide_b = False



        # 碰板反弹
        if (bx - 30 <= self.rect.centerx <= bx + 30) and (362 >= self.rect.y >= 350 - self.rect[3]):
            self.speed = (math.Vector2(self.rect.centerx, self.rect.centery) - math.Vector2(bx, 366)).normalize() * bv
            # print(sqrt(self.speed[0] ** 2 + self.speed[1] ** 2))
            # print(int(self.speed[0]), int(self.speed[1]))
            tern.play()
            # self.speed[1] *= -1

        self.rect.y += self.speed[1]

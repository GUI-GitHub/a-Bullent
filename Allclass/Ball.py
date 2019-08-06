from setting.settings import *
from Allclass.Prop import *


class Ball:
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

            if blk.rect.colliderect(self): #self.rect.x < blk.pos[0] + blk.size[0] and self.rect.x + self.rect.w > blk.pos[0] and self.rect.y < blk.pos[1] + blk.size[1] and self.rect.y + self.rect.h > blk.pos[1]:
                bam.play()

                if (self.rect.y <= blk.pos[1] + blk.size[1] or self.rect.y + self.rect.h >= blk.pos[1]):  # and not self.inb:
                    #碰左右壁
                    self.speed[0] = -self.speed[0]

                if (self.rect.x <= blk.pos[0] + blk.size[0] or self.rect.x + self.rect.w >= blk.pos[0])and not self.collide_b:#and not self.inb:
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
        if Rect(bx - 30, 350, 60, 12).colliderect(self):
            self.speed = (math.Vector2(self.rect.centerx, self.rect.centery) - math.Vector2(bx, 366)).normalize() * bv
            tern.play()
            # self.speed[1] *= -1

        self.rect.y += self.speed[1]

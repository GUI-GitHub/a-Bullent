from setting.settings import *
from Allclass.BallGroup import *

class Prop:
    def __init__(self, type, pos):
        self.type = type
        self.type1 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_two.png"))
        self.type2 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_double.png"))
        if self.type == 1:
            self.image = self.type1
        elif self.type == 2:
            self.image = self.type2
        else:
            self.image = 0
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)

    def move(self, bx, ballg):
        self.rect = self.rect.move((0, pv))

        #道具事件
        if (bx - 30 - self.rect.w*0.5 <= self.rect.centerx <= bx + 30 + self.rect.w*0.5) and (self.rect.y >= 350 - self.rect.h):
            if self.type == 1:
                ballg.add_demo(tuple(math.Vector2(1, 1).normalize()*bv), pos=(bx-4, 350-16))
                ballg.add_demo(tuple(math.Vector2(-1, 1).normalize() * bv), pos=(bx - 4, 350 - 16))
            elif self.type == 2:
                add = []
                for ball in ballg.balls:
                    v1 = math.Vector2(ball.speed).rotate(45).normalize()*bv
                    add.append(ballg.demo(tuple(v1), ball.rect[:2]))
                    v2 = math.Vector2(ball.speed).rotate(-45).normalize() * bv
                    add.append(ballg.demo(tuple(v2), ball.rect[:2]))

                ballg.adds(add)

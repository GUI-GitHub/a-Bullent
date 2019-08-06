from setting.settings import *
from Allclass.Ball import *

class Prop:
    def __init__(self, type, pos):
        self.type = type
        self.type0 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_two.png"))
        self.type1 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_double.png"))
        if self.type == 0:
            self.image = self.type0
        elif self.type == 1:
            self.image = self.type1
        else:
            self.image = 0
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)

    def move(self, bx, ballg):
        self.rect.move((0, pv))

        #道具事件
        if (bx - 30 <= self.rect.centerx <= bx + 30) and (self.rect.y >= 350 - self.rect.h):
            if type == 0:
                ballg.add(Ball(tuple(math.Vector2(1, 1).normalize()*bv), pos=(bx-4, 350-16)))
                ballg.add(Ball(tuple(math.Vector2(-1, 1).normalize() * bv), pos=(bx - 4, 350 - 16)))
            elif type == 1:
                addball = []
                for ball in ballg:
                    addball.append(Ball((bv, bv), ball.rect[:2]))
                    addball.append(Ball((bv, -bv), ball.rect[:2]))
                    addball.append(Ball((-bv, bv), ball.rect[:2]))
                    addball.append(Ball((-bv, -bv), ball.rect[:2]))
                ballg.adds(addball)




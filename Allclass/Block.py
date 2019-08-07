from setting.settings import *


class Block(sprite.Sprite):
    def __init__(self, pos, type, size=(20, 20), count=1, color=(127, 127, 127)):
        self.pos = pos
        self.type = type
        self.size = size
        self.count = count
        self.color = color
        self.rect = Rect(pos, size)

    def draw(self):
        draw.rect(screen, self.color, self.pos+self.size, 0)
        #f1.render_to(screen, (self.pos[0]+3, self.pos[1]), str(self.type))

    def __repr__(self):
        return "pos:%s,color:%s,size:%s,type:%s" % (self.pos, self.color, self.size, self.type)
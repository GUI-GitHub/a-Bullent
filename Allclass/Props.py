from setting.settings import *


class Props:
    def __init__(self, props):
        self.props = []
        self.props += props

    def add(self, props):
        self.props.append(props)

    def draw(self, bx, ballg):
        for prop in self.props:
            prop.move(bx, ballg)
            screen.blit(prop.image, prop.rect)
            if (bx - 30 <= prop.rect.centerx <= bx + 30) and (prop.rect.y >= 350 - prop.rect.h):
                self.props.remove(prop)

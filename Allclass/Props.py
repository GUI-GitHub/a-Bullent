from setting.settings import *


class Props:
    def __init__(self, props):
        self.props = []
        self.props += props

    def add(self, props):
        self.props.append(props)

    def draw(self, bx, ballg, blood):
        for prop in self.props:
            prop.move(bx, ballg, blood)
            screen.blit(prop.image, prop.rect)
            if (Rect(bx-40, 500, 80, 15).colliderect(prop.rect)) or prop.rect.y > HEIGHT:
                self.props.remove(prop)

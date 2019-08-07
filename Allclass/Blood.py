from setting.settings import *


class Blood:
    def __init__(self, num):
        self.image = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/blood.png"))
        self.rect = self.image.get_rect()
        self.num = num

    def draw(self):
        for i in range(self.num):
            screen.blit(self.image, (i*17+2, 0))

from setting.settings import *


class Cannon:
    def __init__(self, pos):
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/c.png")
        self.image = image.load(image_path)
        self.image_show = self.image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.move_ip(pos[0]-22, pos[1]-22)

    def draw(self, pos):
        a = (math.Vector2(pos)-math.Vector2(self.rect.centerx, self.rect.centery-5)).angle_to((0, 0))
        self.image_show = transform.rotate(self.image, a+270)
        screen.blit(self.image_show, self.rect)

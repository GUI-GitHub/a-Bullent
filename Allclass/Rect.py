from setting.settings import *
class Rect():

    @staticmethod
    def rect(screen, x, y):
        rect_color = (255, 255, 0)
        # 定义board
        pos = x - 30, y, 60, 12
        draw.rect(screen, rect_color, pos)

import pygame,sys
from pygame.locals import *

pygame.init()

window_Surface = pygame.display.set_mode((255, 255), 0, 32)
pygame.display.set_caption('start')
def run():
    #RBG这里是调节颜色的
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    #fonts，字体大小
    basic_Font = pygame.font.SysFont(None, 16)

    text = basic_Font.render('Click anywhere on the screen to start', True, WHITE, BLUE)
    text_Rect = text.get_rect()

    text_Rect.centerx = window_Surface.get_rect().centerx
    text_Rect.centery = window_Surface.get_rect().centery
    window_Surface.fill(WHITE)

    pygame.draw.polygon(window_Surface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    pygame.draw.line(window_Surface, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(window_Surface, BLUE, (120, 60), (60, 120))
    pygame.draw.line(window_Surface, BLUE, (60, 120), (120, 120), 4)

    pygame.draw.circle(window_Surface, BLUE, (300, 50), 20, 1)

    pygame.draw.ellipse(window_Surface, RED, (300, 250, 40, 80), 1)

    pygame.draw.rect(window_Surface, RED,
                     (text_Rect.left - 20,
                      text_Rect.top - 20,
                      text_Rect.width + 40,
                      text_Rect.height + 40))

    pixArry = pygame.PixelArray(window_Surface)
    pixArry[230][180] = BLACK
    del pixArry
    window_Surface.blit(text, text_Rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                #如果要加第三个页面这需要在这里判断判断鼠标的点击位置。然后通过位置做判断
                return 0
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

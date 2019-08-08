import pygame, sys, os
from pygame.locals import *
from setting.settings import *
import Allclass.window as win

win.fail()

window_Surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('start')


def run():
    # RBG这里是调节颜色的
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    window_Surface.fill(WHITE)

    pygame.draw.polygon(window_Surface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(window_Surface, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(window_Surface, BLUE, (120, 60), (60, 120))
    pygame.draw.line(window_Surface, BLUE, (60, 120), (120, 120), 4)
    pygame.draw.circle(window_Surface, BLUE, (300, 50), 20, 1)
    pygame.draw.ellipse(window_Surface, RED, (300, 250, 40, 80), 1)

    # 绘制标题
    f2.render_to(window_Surface, (35, 50), "A bullent")
    # 绘制按钮
    text, text_Rect = f3.render("     开始     ", size=40)
    menu, menu_Rect = f3.render("     选关     ", size=30)
    text_Rect.centerx = window_Surface.get_rect().centerx
    text_Rect.centery = window_Surface.get_rect().centery
    menu_Rect.centerx = text_Rect.centerx
    menu_Rect.centery = text_Rect.centery + 100
    pygame.draw.rect(window_Surface, (216, 152, 0),
                     (text_Rect.left - 10,
                      text_Rect.top - 10,
                      text_Rect.width + 40,
                      text_Rect.height + 40))
    pygame.draw.rect(window_Surface, (255, 180, 0),
                     (text_Rect.left - 20,
                      text_Rect.top - 20,
                      text_Rect.width + 40,
                      text_Rect.height + 40))
    pygame.draw.rect(window_Surface, (71, 204, 204),
                     (menu_Rect.left - 10,
                      menu_Rect.top - 10,
                      menu_Rect.width + 40,
                      menu_Rect.height + 40))
    pygame.draw.rect(window_Surface, (89, 255, 255),
                     (menu_Rect.left - 20,
                      menu_Rect.top - 20,
                      menu_Rect.width + 40,
                      menu_Rect.height + 40))
    window_Surface.blit(text, text_Rect)
    window_Surface.blit(menu, menu_Rect)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                # 如果要加第三个页面这需要在这里判断判断鼠标的点击位置。然后通过位置做判断
                if Rect(text_Rect.left - 20, text_Rect.top - 20, text_Rect.width + 40,
                        text_Rect.height + 40).collidepoint(event.pos):
                    pass
                elif Rect(menu_Rect.left - 20, menu_Rect.top - 20, menu_Rect.width + 40,
                          menu_Rect.height + 40).collidepoint(event.pos):
                    pass
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

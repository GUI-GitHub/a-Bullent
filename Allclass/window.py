from setting.settings import *


menu = transform.scale2x(image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/menu_ico.png")))
retry = transform.scale2x(image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/retry_ico.png")))
goon = transform.scale2x(image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/goon_ico.png")))

menu_rect = menu.get_rect()
retry_rect = retry.get_rect()
goon_rect = goon.get_rect()

menu_rect.centerx = screen_rect.centerx-100
menu_rect.centery = 450

retry_rect.centerx = screen_rect.centerx
retry_rect.centery = 450

goon_rect.centerx = screen_rect.centerx+100
goon_rect.centery = 450

def winv(tn):

    for i in range(0, floor(tn / 9), floor(tn/9/10)):
        screen.fill((255, 255, 255))
        text = f3.render("用时" + str(i/10) + "秒",size=60)
        text[1].centerx = screen_rect.centerx
        text[1].centery = 150
        d.play()
        time.delay(100)
        screen.blit(text[0], text[1])
        display.update()
    while not mixer.get_busy():
        win.play()
        break

    screen.blit(menu, menu_rect)
    screen.blit(retry, retry_rect)
    screen.blit(goon, goon_rect)

    while 1:
        for e in event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONUP:
                if menu_rect.collidepoint(e.pos):
                    return 0
                elif retry_rect.collidepoint(e.pos):
                    return 1
                elif goon_rect.collidepoint(e.pos):
                    return 2

        display.update()


def fail():
    text = f3.render("失败",size=60)
    text[1].centerx = screen_rect.centerx
    text[1].centery = 150
    screen.blit(text[0], text[1])
    screen.blit(menu, menu_rect)
    screen.blit(retry, retry_rect)

    while 1:
        for e in event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONUP:
                if menu_rect.collidepoint(e.pos):
                    return 0
                elif retry_rect.collidepoint(e.pos):
                    return 1

        display.update()


def menus():
    mask = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/menu_map_mask.png"))
    map_dict = []
    for i, file in enumerate(map_files):
        map = transform.scale2x(image.load(file))

        pos_mask = (i % 3)*125+25, (i//3)*125+25+50
        pos_map = (i % 3)*125+20+25, (i//3)*125+20+25+50

        mask_rect = mask.get_rect()
        mask_rect.move_ip(pos_mask)

        screen.blit(mask, mask_rect)
        screen.blit(map, pos_map)

        map_dict.append((i, mask_rect))

    display.update()

    while 1:
        for e in event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONUP:
                for i, mask_rect in map_dict:
                    if mask_rect.collidepoint(e.pos):
                        return i

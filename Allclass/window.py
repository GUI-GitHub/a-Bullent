from setting.settings import *


menu = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/menu_ico.png"))
retry = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/retry_ico.png"))
goon = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/goon_ico.png"))

menu_rect = menu.get_rect()
retry_rect = retry.get_rect()
goon_rect = goon.get_rect()

menu_rect.move_ip(80, 250)
retry_rect.move_ip(130, 250)
goon_rect.move_ip(180, 250)

def winv(tn):

    for i in range(0, floor(tn / 9), floor(tn/9/10)):
        screen.fill((255, 255, 255))
        f3.render_to(screen, (75, 100), "用时" + str(i/10) + "秒")
        d.play()
        time.delay(100)
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



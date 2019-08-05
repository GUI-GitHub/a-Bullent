from setting.settings import *

class BallGroup():

    def __init__(self, balls=[]):
        self.balls = balls#所有小球

    def add(self, ball):
        self.balls.append(ball)

    def move(self, bx, blocks):
        for ball in self.balls:
            ball.move(bx, blocks)#移动单个小球

            screen.blit(ball.image, ball.rect)
            #f1.render_to(screen, ball.rect[:2], str(ball.speed),fgcolor=(255,255,255))
            # 掉入后删除小球
            if ball.rect[1] > 400 - ball.rect[3] or ball.rect[0] <= -ball.rect[2] or ball.rect[0] >= WIDTH or ball.rect[1] <= -ball.rect[1]*0.5:
                self.balls.remove(ball)

from setting.settings import *
from Allclass.Ball import *

class BallGroup():

    def __init__(self, balls=[]):
        self.balls = balls#所有小球

    def add(self, ball):
        self.balls.append(ball)

    def adds(self, balls):
        self.balls += balls

    def add_demo(self, speed, pos):
        self.add(Ball(speed, pos=pos))

    def move(self, bx, blocks):
        for ball in self.balls:
            ball.move(bx, blocks)#移动单个小球

            screen.blit(ball.image, ball.rect)
            # 掉入后删除小球
            #print(ball.rect,ball.collide_wx)
            if ball.rect.y > HEIGHT - ball.rect.h:# or ball.rect.x <= -ball.rect.w or ball.rect.x >= WIDTH:

                self.balls.remove(ball)
                if len(self.balls) == 0:
                    # 失败
                    los.play()


    @staticmethod
    def demo(speed, pos):
        return Ball(speed, pos=pos)
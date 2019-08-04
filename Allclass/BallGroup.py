from setting.settings import *
class BallGroup():

    def __init__(self, balls=[]):
        self.balls = balls

    def add(self, ball):
        self.balls.append(ball)

    def move(self, bx, blocks):
        for ball in self.balls:
            ball.move(bx, blocks)

            screen.blit(ball.image, ball.rect)

            # 掉入后删除ball
            if ball.rect[1] > 400 - 16 or ball.rect[0] <= -16 or ball.rect[0] >= WIDTH or ball.rect[1] <= -8:
                self.balls.remove(ball)
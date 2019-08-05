from setting.settings import *
from Allclass import BallGroup,Blocks,Ball,Rect

def run():
    shooted=0

    gtime=time.Clock()#游戏时间设置
    bx = 150#设置开始时板的位置
    ballg = BallGroup.BallGroup()
    blocks = Blocks.Blocks.generator("rect", height=10, width=20,dpos=(0,50))#方块生成
    #blocks.adds(Blocks.Blocks.generator("rect", height=2, width=20,dpos=(0,370)))
    while 1:

        gtime.tick(t)
        screen.fill((0,0,0))

        for i in event.get():
            if i.type == QUIT:
                exit(0)
            if i.type == MOUSEMOTION:
                #鼠标控制 板
                if shooted:
                    bx = i.pos[0]
            if i.type == MOUSEBUTTONDOWN or (i.type == KEYDOWN and i.key==K_SPACE):
                #发射小球
                if not shooted:
                    a= (math.Vector2(i.pos)-math.Vector2(150,350)).normalize()*bv
                    ballg.add(Ball.Ball(tuple(a),pos=(bx-4,350-16)))
                    shooted=1

        Rect.Rect.rect(screen, bx, 350)#画出板
        blocks.draw()#画出方块
        ballg.move(bx, blocks)#移动所有小球并画出

        display.flip()
        display.update()



from setting.settings import *
from Allclass import BallGroup,Blocks,Ball,Rect,Props


def run():
    shooted = 0
    tn = 0

    gtime = time.Clock()#游戏时间设置
    bx = 150#设置开始时板的位置
    ballg = BallGroup.BallGroup()
    props = Props.Props([])
    blocks = Blocks.Blocks.generator("rect", height=5, width=33, dpos=(0, 50), size=(7, 7))#方块生成

    while 1:
        gtime.tick(t)
        screen.fill((255, 255, 255))
        for i in event.get():
            if i.type == QUIT:
                exit(0)
            if i.type == MOUSEMOTION:
                #鼠标控制 板
                if shooted:
                    bx = i.pos[0]
            if i.type == MOUSEBUTTONDOWN:
                #发射小球
                if not shooted:
                    a = (math.Vector2(i.pos)-math.Vector2(150, 350)).normalize()*bv
                    ballg.add(Ball.Ball(tuple(a), pos=(bx-4, 350-16)))
                    shooted = 1

        if len(blocks.blocks) == 0: #成功

            f3.render_to(screen, (50, 100), "用时"+str(floor(tn/9)/10)+"秒")
            if shooted:
                win.play()
                shooted = not shooted

            #screen.fill((127, 127, 127, 127))
        else:
            Rect.Rect.rect(screen, bx, 350)  # 画出板
            props.draw(bx, ballg)
            blocks.draw(props)  # 画出方块
            ballg.move(bx, blocks)  # 移动所有小球并画出
            tn += 1


        display.flip()
        display.update()



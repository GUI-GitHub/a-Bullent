from setting.settings import *
from Allclass import BallGroup, Blocks, Ball, Rect, Props, Block, Blood, window














def run(file):
    if 1:
        pixarray = PixelArray(image.load(file))

        shooted = 0
        parbegin = 0

        tn = 0

        gtime = time.Clock()#游戏时间设置
        bx = screen_rect.centerx#设置开始时板的位置
        blood = Blood.Blood(3)
        ballg = BallGroup.BallGroup()
        props = Props.Props([])
        #blocks = Blocks.Blocks.generator("rect", height=5, width=33, dpos=(0, 50), size=(8, 8))#方块生成
        blocks = Blocks.Blocks.convert(pixarray)

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
                        parbegin = 1

            if len(blocks.blocks) == 0: #成功
               return 1
            else:
                Rect.Rect.rect(screen, bx, 450)  # 画出板
                props.draw(bx, ballg, blood)
                blocks.draw(props)  # 画出方块
                ballg.move(bx, blocks)  # 移动所有小球并画出
                blood.draw()
                tn += 1

            if len(ballg.balls) == 0 and parbegin and shooted:
                # 失败
                los.play()
                shooted = 0
                if not blood.num:
                    parbegin = 0
                    return 0
                blood.num -= 1


            #print(len(ballg.balls), ballg.db)
            display.flip()
            display.update()

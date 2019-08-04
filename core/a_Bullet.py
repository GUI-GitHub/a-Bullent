from setting.settings import *
from Allclass import BallGroup,Blocks,Ball,Rect

def run():
    gtime=time.Clock()
    shooted=0
    #board x
    bx=150
    ballg=BallGroup.BallGroup()
    blocks=Blocks.Blocks.generator("rect",height=10,width=16)
    #blocks=Blocks([Block((150,150),1,(30,30)),Block((150,110),1,(30,30))])
    while 1:

        gtime.tick(150)
        screen.fill((0,0,0))

        #

        for i in event.get():

            if i.type==QUIT:
                exit(0)
            if i.type==MOUSEMOTION:
                #board set
                bx=i.pos[0]

            if 1:# i.type==MOUSEBUTTONDOWN or (i.type==KEYDOWN and i.key==K_SPACE) :
                ballg.add(Ball.Ball((0,-3),pos=(bx-4,350-16)))

        Rect.Rect.rect(screen,bx,350)

        blocks.draw()        
        ballg.move(bx,blocks)
        display.flip()
        display.update()



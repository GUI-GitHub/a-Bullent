from pygame import *
import pygame.freetype
import random
from math import *

#define

HEIGHT=400
WIDTH=320

#init
init()
screen=display.set_mode([WIDTH,HEIGHT],0,32)
display.set_caption("game")
screen.fill((0,0,0))
f1=pygame.freetype.Font("C:\\Windows\\Fonts\\comic.ttf",20)



class Ball():
    def __init__(self,speed,pos=(0,0)):
        self.image=image.load("b.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.speed=list(speed)
    def move(self,bx,blocks):
        #碰壁反弹
        if self.rect[0]<=0+1 or self.rect[0]>=WIDTH-16-1:
            self.speed[0]=-self.speed[0]
        if self.rect[1]<=0+1:
            self.speed[1]=-self.speed[1]
        
        #碰板反弹
        if (bx-30<self.rect[0]+8<bx+30)and(362>self.rect[1]>350-16):
            #print("in the right range")
            #board=(bx,350)
            ball=self.rect[0:2]
            dx=(ball[0]+8-bx)
            
            #dy=ball[1]+8-340
            r=30
            d=0.2
            
            #print(dx)
            self.speed=[dx*d,-sqrt(abs(r**2-dx**2))*d]
            print(sqrt(self.speed[0]**2+self.speed[1]**2))

        #碰砖反弹
        for blk in blocks.blocks:
            rblk=(blk.pos[0]+blk.size[0]*0.5,blk.pos[1]+blk.size[1]*0.5)

            ballpos=self.rect[0:2]
            rball=(ballpos[0]+8,ballpos[1]+8)
            #  碰右壁                                碰左壁                       碰下壁                                碰上壁
            if ballpos[0]<blk.pos[0]+blk.size[0] and ballpos[0]+16>blk.pos[0] and ballpos[1]<blk.pos[1]+blk.size[1] and ballpos[1]+16>blk.pos[1]:
                if not rball[0]==rblk[0]:
                    self.speed[0]=-self.speed[0]
                if not rball[1]==rblk[1]:
                    self.speed[1]=-self.speed[1]

                #if not blk.type==4:
                #print(ballpos,blk)
                blk.type=blk.type-1
                    #blocks.blocks.remove(blk)
                break
        #print(self.speed,self.rect)
        self.rect=self.rect.move(self.speed)
        
class BallGroup():
    
    def __init__(self,balls=[]):
        self.balls=balls

    def add(self,ball):
        self.balls.append(ball)

    def move(self,bx,blocks):
        for ball in self.balls:
            ball.move(bx,blocks)
            
            screen.blit(ball.image,ball.rect)

            #掉入后删除ball
            if ball.rect[1]>400-16 or ball.rect[0]<=-16 or ball.rect[0]>=WIDTH or ball.rect[1]<=-8:
                self.balls.remove(ball)

class Block():
    def __init__(self,pos,type,size=(20,20)):
        self.pos=pos
        self.type=type
        self.size=size
    def draw(self):
        if self.type==1:
            self.color=(255,0,0)
        elif self.type==2:
            self.color=(255,255,0)
        elif self.type==3:
            self.color=(255,255,255)

        else:
            self.color=(127,127,127)
        
        draw.rect(screen,self.color,self.pos+self.size,0)
        f1.render_to(screen,(self.pos[0]+3.5,self.pos[1]),str(self.type),fgcolor=(0,0,0))
        #print("draw")
    def __repr__(self):
        return "pos:%s,color:%s,size:%s,type:%s"%(self.pos,self.color,self.size,self.type)

class Blocks():
    def __init__(self,blocks=[]):
        self.blocks=blocks
    def draw(self):
        for block in self.blocks:
            if block.type>0:
                block.draw()
            else:
                self.blocks.remove(block)
    @classmethod
    def generator(self,mode,*arg,**kw):
        blocks=[]
        print(mode)
        if mode=="rect":
            for i in range(kw["height"]):
                for j in range(kw["width"]):
                    blocks.append(Block((j*20,i*20),random.randint(0,4),size=(16,16)))
        #print(blocks)
        return Blocks(blocks)

#rectangle
def rect(screen,x,y):
    rect_color=(255,255,0)
    #定义board
    pos=x-30,y,60,12
    draw.rect(screen,rect_color,pos,5)

if __name__=="__main__":
    
    gtime=time.Clock()

    shooted=0
    
    #board x
    bx=150
    ballg=BallGroup()
    blocks=Blocks.generator("rect",height=10,width=16)
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
                
            if i.type==MOUSEBUTTONDOWN or (i.type==KEYDOWN and i.key==K_SPACE) :
                ballg.add(Ball((0,-5),pos=(bx-8,350-16)))

        rect(screen,bx,350)
        
        blocks.draw()        
        ballg.move(bx,blocks)
        #display.flip()
        display.update()



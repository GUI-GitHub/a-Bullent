from setting.settings import  *
from Allclass.Block import Block
class Blocks():
    def __init__(self,blocks=[]):
        self.blocks=blocks


    def adds(self,blocks):
        self.blocks+=blocks
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
                    blocks.append(Block((j*20,i*20),random.randint(0,15),size=(16,16)))
        #print(blocks)
        return Blocks(blocks)
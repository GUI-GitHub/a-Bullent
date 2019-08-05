from setting.settings import  *
from Allclass.Block import Block
class Blocks():
    def __init__(self, blocks=[]):
        self.blocks = blocks

    def adds(self, blocks):
        self.blocks = blocks.blocks + self.blocks

    def draw(self):
        for block in self.blocks:
            if block.type > 0:
                block.draw()
            else:
                self.blocks.remove(block)

    @staticmethod
    def generator(mode, *arg, **kw):
        blocks = []
        print(mode)
        if "size" in kw.keys():
            size = kw["size"]
        else:
            size = (16, 16)
        if "dpos" in kw.keys():
            dpos = kw["dpos"]
        else:
            dpos = (0, 0)
        if mode == "rect":
            for i in range(kw["height"]):
                for j in range(kw["width"]):
                    blocks.append(Block((j*size[0]+dpos[0], i*size[1]+dpos[1]), 1,size=size))
        #print(blocks)
        return Blocks(blocks)

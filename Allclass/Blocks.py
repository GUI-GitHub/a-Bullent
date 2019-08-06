from setting.settings import *
from Allclass.Block import Block
from Allclass.Prop import Prop

class Blocks:
    def __init__(self, blocks=[]):
        self.blocks = blocks

    def adds(self, blocks):
        self.blocks = blocks.blocks + self.blocks

    def draw(self, props):
        for block in self.blocks:
            if block.count > 0:
                block.draw()
            else:
                self.blocks.remove(block)
                if block.type:
                    props.add(Prop(block.type, block.pos))

    @staticmethod
    def generator(mode, *arg, **kw):
        blocks = []
        print(mode)
        if "size" in kw.keys():
            size = kw["size"]
        else:
            size = (9, 9)
        if "dpos" in kw.keys():
            dpos = kw["dpos"]
        else:
            dpos = (0, 0)
        if mode == "rect":
            for i in range(kw["height"]):
                for j in range(kw["width"]):
                    blocks.append(Block((j*size[0]+dpos[0], i*size[1]+dpos[1]), random.randint(0, 2), size=size))
        #print(blocks)
        return Blocks(blocks)

from setting import *
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self,asset,color,pos,flip=False):
        super().__init__()
        self.asset=asset
        self.image=self.asset.pipe_images[color]
        self.image=pygame.transform.flip(self.image,False,flip)
        self.rect=self.image.get_rect(left=SCREEN_WIDTH,bottom=pos)
        self.rect.size[1]
    
    def update(self):
        self.rect.x-=1*SCALE
        if self.rect.right<0:
            self.kill()
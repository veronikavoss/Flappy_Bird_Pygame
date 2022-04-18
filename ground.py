from setting import *

class Ground(pygame.sprite.Sprite):
    def __init__(self,asset):
        super().__init__()
        self.asset=asset
        self.image=self.asset.stage_images['ground']
        self.rect=self.image.get_rect(bottom=SCREEN_HEIGHT)
        self.speed=-3
    
    def update(self):
        self.rect.move_ip(self.speed,0)
        if self.rect.right<SCREEN_WIDTH:
            self.rect.left=0
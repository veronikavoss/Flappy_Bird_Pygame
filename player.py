from setting import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,asset):
        super().__init__()
        self.asset=asset
        self.color=random.choice(list(self.asset.player_images.keys()))
        self.frame_index=0
        self.image=self.asset.player_images[self.color][self.frame_index]
        self.rect=self.image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
        self.move_speed=0
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        
        if key_input[pygame.K_LEFT]:
            self.move_speed=-3
        elif key_input[pygame.K_RIGHT]:
            self.move_speed=3
        else:
            self.move_speed=0
        
        self.rect.move_ip(self.move_speed,0)
    
    def update(self):
        self.set_key_input()
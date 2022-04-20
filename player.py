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
        self.direction=pygame.math.Vector2(0,0)
        self.gravity=0.2*SCALE
        self.jump_speed=-3.3*SCALE
        
        self.player_status='ready'
        self.jump_pressed=False
    
    def set_gravity(self):
        self.rect.y+=self.direction.y
        self.direction.y+=self.gravity
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_RIGHT]:
            if not self.jump_pressed:
                self.direction.y=self.jump_speed
                self.jump_pressed=True
        else:
            self.jump_pressed=False
    
    def update(self):
        mouse_input=pygame.mouse.get_pressed()
        
        if mouse_input[0]:
            self.player_status='playing'
        if self.player_status=='playing':
            self.set_gravity()
            self.set_key_input()
from setting import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,asset):
        super().__init__()
        self.asset=asset
        self.color=random.choice(list(self.asset.player_images.keys()))
        self.frame_index=0
        self.image=self.asset.player_images[self.color][self.frame_index]
        self.original_image=self.image
        self.rect=self.image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2.2))
        self.direction=pygame.math.Vector2(0,0)
        self.gravity=0.2*SCALE
        self.jump_speed=-3.3*SCALE
        
        self.game_status='start_screen' # start_screen,ready_screen,playing_game
        self.player_status='idle' # idle,playing,crash,falling
        self.jump_pressed=False
    
    def set_idle_animate(self):
        if self.player_status=='idle':
            if pygame.time.get_ticks()//500%2==0:
                self.rect.y+=1
            else:
                self.rect.y-=1
    
    def animate(self):
        if self.player_status!='crash' and self.player_status!='die':
            animation=self.asset.player_images[self.color]
            self.frame_index+=0.1
            if self.frame_index>=len(animation):
                self.frame_index=0
            self.image=animation[int(self.frame_index)]
            self.image=pygame.transform.rotate(self.image,max(-self.direction.y*4,-90))
        else:
            self.image=self.original_image
            self.image=pygame.transform.rotate(self.image,-90)
    
    def set_gravity(self):
        if self.player_status=='playing' or self.player_status=='crash':
            self.rect.y+=self.direction.y
            self.direction.y+=self.gravity
    
    def set_key_input(self):
        if self.game_status=='playing_game' and self.player_status=='playing':
            key_input=pygame.key.get_pressed()
            if key_input[pygame.K_SPACE] or key_input[pygame.K_RIGHT]:
                if not self.jump_pressed:
                    self.direction.y=self.jump_speed
                    self.jump_pressed=True
            else:
                self.jump_pressed=False
    
    def update(self):
        self.set_idle_animate()
        self.animate()
        self.set_gravity()
        self.set_key_input()
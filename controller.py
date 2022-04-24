from setting import *
from pipe import Pipe
from ground import Ground
from player import Player
from ui import Ui
import random

class Controller(Ui):
    def __init__(self,screen,asset):
        Ui.__init__(self,asset)
        self.screen=screen
        self.asset=asset
        
        self.set_sky_image()
        self.pipe_color=random.choice(('red','green'))
        self.update_pipe_spawn_timer=0
        self.pipe=pygame.sprite.Group()
        self.ground=pygame.sprite.GroupSingle(Ground(self.asset))
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
        
        self.score=0
    
    def set_game_start(self):
        # start_screen
        if self.player.sprite.game_status=='start_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.start_play_button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.player.sprite.game_status='ready_screen'
        
        # ready_screen
        if self.player.sprite.game_status=='ready_screen':
            key_input=pygame.key.get_pressed()
            if key_input[pygame.K_SPACE] or key_input[pygame.K_RIGHT]:
                self.player.sprite.game_status='playing_game'
                self.player.sprite.player_status='playing'
    
    def set_sky_image(self):
        sky=random.choice(list(self.asset.stage_images['sky'].keys()))
        self.sky_image=self.asset.stage_images['sky'][sky]
    
    def pipe_spawn_timer(self):
        self.update_pipe_spawn_timer=pygame.time.get_ticks()
    
    def spawn_pipe(self):
        current_time=pygame.time.get_ticks()
        if current_time-self.update_pipe_spawn_timer>=1300:
            pipe_height=random.choice((
                SKY_HEIGHT//5-PLAYER_HEIGHT*2,
                SKY_HEIGHT//5*2-PLAYER_HEIGHT*2,
                SKY_HEIGHT//5*3-PLAYER_HEIGHT*2,
                SKY_HEIGHT//5*4-PLAYER_HEIGHT*2
            ))
            top_pipe=Pipe(self.asset,self.pipe_color,pipe_height,True)
            bottom_pipe=Pipe(self.asset,self.pipe_color,top_pipe.rect.bottom+160*SCALE+PLAYER_HEIGHT*4)
            self.pipe.add(top_pipe,bottom_pipe)
            self.pipe_spawn_timer()
    
    def update(self):
        self.spawn_pipe()
        self.pipe.update()
        self.ground.update()
        self.player.update()
        self.set_game_start()
        self.tap_image_animate()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.sky_image,(0,0))
        self.pipe.draw(self.screen)
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
        self.start_screen_draw(self.screen)
        self.ready_screen_draw(self.screen)
        self.score_draw(self.screen,self.score)
        pygame.draw.circle(self.screen, 'red', (SKY_WIDTH//2,SKY_HEIGHT//2), 2, width=5)
        print(self.player.sprite.game_status)
        print(self.pipe)
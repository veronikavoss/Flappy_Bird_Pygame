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
        self.ready_position=True
        
        self.score=0
        self.best_score=False
        self.scoring=False
    
    def open_high_score(self):
        with open('high_score.txt','r') as r:
            high_score=r.readline()
            return int(high_score)
    
    def save_high_score(self):
        with open('high_score.txt','w') as w:
            w.write(str(self.score))
    
    def set_play_button(self):
        # start_screen
        if self.player.sprite.game_status=='start_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.play_button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.player.sprite.game_status='ready_screen'
        # game_over__screen
        elif self.player.sprite.game_status=='game_over_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.play_button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.__init__(self.screen,self.asset)
                    self.player.sprite.game_status='ready_screen'
    
    def set_ready_screen(self):
        # ready_screen
        if self.player.sprite.game_status=='ready_screen':
            if self.ready_position:
                self.player.sprite.set_position()
                self.ready_position=False
            key_input=pygame.key.get_pressed()
            if key_input[pygame.K_SPACE] or key_input[pygame.K_RIGHT]:
                self.player.sprite.game_status='playing_game'
                self.player.sprite.player_status='playing'
                self.ready_position=True
    
    def set_sky_image(self):
        sky=random.choice(list(self.asset.stage_images['sky'].keys()))
        self.sky_image=self.asset.stage_images['sky'][sky]
    
    def pipe_spawn_timer(self):
        self.update_pipe_spawn_timer=pygame.time.get_ticks()
    
    def spawn_pipe(self):
        if self.player.sprite.game_status=='playing_game' and self.player.sprite.player_status=='playing':
            current_time=pygame.time.get_ticks()
            if current_time-self.update_pipe_spawn_timer>=1300:
                pipe_height=random.choice((
                    SKY_HEIGHT//9*3-PLAYER_HEIGHT*2.5,
                    SKY_HEIGHT//9*4-PLAYER_HEIGHT*2.5,
                    SKY_HEIGHT//9*5-PLAYER_HEIGHT*2.5,
                    SKY_HEIGHT//9*6-PLAYER_HEIGHT*2.5
                ))
                top_pipe=Pipe(self.asset,self.pipe_color,pipe_height,True)
                bottom_pipe=Pipe(self.asset,self.pipe_color,top_pipe.rect.bottom+160*SCALE+PLAYER_HEIGHT*5,index=1)
                self.pipe.add(top_pipe,bottom_pipe)
                self.pipe_spawn_timer()
    
    def set_score(self):
        for pipe in self.pipe:
            if pipe.index:
                if self.player.sprite.rect.left>=pipe.rect.left:
                    self.score+=1
                    pipe.index=None
    
    def collision(self):
        player_collide_pipe=pygame.sprite.spritecollideany(self.player.sprite,self.pipe,pygame.sprite.collide_mask)
        player_collide_ground=pygame.sprite.collide_mask(self.player.sprite,self.ground.sprite)
        if player_collide_pipe:
            self.player.sprite.player_status='crash'
        if player_collide_ground:
            self.player.sprite.player_status='die'
            self.player.sprite.game_status='game_over_screen'
            self.player.sprite.gravity=0
            self.player.sprite.rect.bottom=SKY_HEIGHT-(PLAYER_WIDTH-PLAYER_HEIGHT)
    
    def update(self):
        self.spawn_pipe()
        self.pipe.update(self.player.sprite.player_status)
        self.ground.update(self.player.sprite.player_status)
        self.player.update()
        self.set_play_button()
        self.set_ready_screen()
        self.tap_image_animate()
        self.set_score()
        self.collision()
        # self.set_game_over()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.sky_image,(0,0))
        self.pipe.draw(self.screen)
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_start_screen()
        self.draw_ready_screen()
        self.draw_game_over()
        self.draw_score()
        # print(self.player.sprite.player_status)
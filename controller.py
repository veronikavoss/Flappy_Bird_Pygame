from setting import *
from pipe import Pipe
from ground import Ground
from player import Player
from ui import Ui
import random,time,operator

class Controller(Ui):
    def __init__(self,screen,asset):
        Ui.__init__(self,asset)
        self.screen=screen
        self.asset=asset
        
        self.mouse_status='idle'
        self.set_sky_image()
        self.pipe_color=random.choice(('red','green'))
        self.update_pipe_spawn_timer=0
        self.pipe=pygame.sprite.Group()
        self.ground=pygame.sprite.GroupSingle(Ground(self.asset))
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
        self.ready_position=False
        
        self.score=0
        self.open_high_score()
        self.best_score=False
        self.reset_high_score=False
        self.scoring=False
        self.crash=False
    
    def set_mouse_status(self):
        if self.mouse_status=='idle':
            if pygame.mouse.get_pressed()[0]:
                self.mouse_status='down'
        elif self.mouse_status=='down':
            if not pygame.mouse.get_pressed()[0]:
                self.mouse_status='up'
        elif self.mouse_status=='up':
            if not pygame.mouse.get_pressed()[0]:
                self.mouse_status='idle'
    
    def open_high_score(self):
        high_score=[]
        with open('high_score.txt','r') as r:
            score_data=r.readlines()
            for score in score_data:
                if score!='\n':
                    high_score.append(score.split())
        high_score.sort(key=operator.itemgetter(0),reverse=True)
        return high_score
    
    def save_high_score(self,score=None):
        if score:
            date=time.localtime()
            with open('high_score.txt','a') as a:
                a.write(f'\n{self.score} {date.tm_year}/{date.tm_mon}/{date.tm_mday} {date.tm_hour}:{date.tm_min}:{date.tm_sec}')
        else:
            with open('high_score.txt','w') as w:
                w.write('')
    
    def set_buttons(self):
        # start_screen_play_button
        if self.player.sprite.game_status=='start_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.play_button_rect.collidepoint(mouse_pos):
                if self.mouse_status=='up':
                    self.asset.swooshing_sound.play()
                    self.player.sprite.game_status='ready_screen'
        # game_over_screen_play_button
        elif self.player.sprite.game_status=='game_over_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.play_button_rect.collidepoint(mouse_pos):
                if self.mouse_status=='up':
                    self.asset.swooshing_sound.play()
                    self.__init__(self.screen,self.asset)
                    self.player.sprite.game_status='ready_screen'
        # ranking_button
        if self.player.sprite.game_status=='start_screen' or self.player.sprite.game_status=='game_over_screen':
            if self.ranking_button_rect.collidepoint(mouse_pos):
                if self.mouse_status=='up':
                    self.asset.swooshing_sound.play()
                    self.player.sprite.game_status='rank_screen'
        # reset_button
        if self.player.sprite.game_status=='rank_screen':
            mouse_pos=pygame.mouse.get_pos()
            if self.reset_button_rect.collidepoint(mouse_pos):
                if self.mouse_status=='up':
                    self.asset.swooshing_sound.play()
                    self.save_high_score()
                    if self.player.sprite.player_status=='die':
                        self.reset_high_score=True
        # back_button
            elif self.back_button_rect.collidepoint(mouse_pos):
                if self.mouse_status=='up':
                    self.asset.swooshing_sound.play()
                    if self.player.sprite.player_status=='idle':
                        self.player.sprite.game_status='start_screen'
                    else:
                        self.player.sprite.game_status='game_over_screen'
    
    def set_ready_screen(self):
        # ready_screen
        if self.player.sprite.game_status=='ready_screen':
            key_input=pygame.key.get_pressed()
            if not self.ready_position:
                self.player.sprite.set_position()
                self.ready_position=True
            if key_input[pygame.K_SPACE] or self.mouse_status=='down':
                self.player.sprite.game_status='playing_game'
                self.player.sprite.player_status='playing'
                self.pipe_spawn_timer()
    
    def set_sky_image(self):
        sky=random.choice(list(self.asset.stage_images['sky'].keys()))
        self.sky_image=self.asset.stage_images['sky'][sky]
    
    def pipe_spawn_timer(self):
        self.update_pipe_spawn_timer=pygame.time.get_ticks()
    
    def spawn_pipe(self):
        if self.player.sprite.game_status=='playing_game' and self.player.sprite.player_status=='playing':
            current_time=pygame.time.get_ticks()
            if not self.pipe:
                time=2000
            else:
                time=1300
            if current_time-self.update_pipe_spawn_timer>=time:
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
                    self.asset.point_sound.play()
    
    def collision(self):
        player_collide_pipe=pygame.sprite.spritecollideany(self.player.sprite,self.pipe,pygame.sprite.collide_mask)
        player_collide_ground=pygame.sprite.collide_mask(self.player.sprite,self.ground.sprite)
        if player_collide_pipe and not self.crash:
            self.player.sprite.player_status='crash'
            self.asset.crash_sound.play()
            self.crash=True
        if player_collide_ground:
            self.player.sprite.player_status='die'
            self.asset.die_sound.play()
            self.player.sprite.game_status='game_over_screen'
            self.player.sprite.gravity=0
            self.player.sprite.rect.bottom=SKY_HEIGHT-(PLAYER_WIDTH-PLAYER_HEIGHT)
    
    def update(self):
        self.spawn_pipe()
        self.pipe.update(self.player.sprite.player_status)
        self.ground.update(self.player.sprite.player_status)
        self.player.update()
        self.set_mouse_status()
        self.set_ready_screen()
        self.tap_image_animate()
        self.set_buttons()
        self.collision()
        self.set_score()
    
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
        self.draw_rank()
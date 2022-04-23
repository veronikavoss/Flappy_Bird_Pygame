from setting import *
from player import Player
from ground import Ground
from ui import Ui
import random

class Controller(Ui):
    def __init__(self,screen,asset):
        Ui.__init__(self,asset)
        self.screen=screen
        self.asset=asset
        
        self.set_sky_image()
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
    
    def update(self):
        self.ground.update()
        self.player.update()
        self.set_game_start()
        self.tap_image_animate()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.sky_image,(0,0))
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
        self.start_screen_draw(self.screen)
        self.ready_screen_draw(self.screen)
        self.score_draw(self.screen,self.score)
        
        print(self.player.sprite.game_status)
from setting import *
from player import Player
from ground import Ground
import random

class Controller:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        
        self.set_stage()
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
    
    def set_stage(self):
        sky=random.choice(list(self.asset.stage_images['sky'].keys()))
        self.sky=self.asset.stage_images['sky'][sky]
        self.ground=pygame.sprite.GroupSingle(Ground(self.asset))
    
    def update(self):
        self.ground.update()
        self.player.update()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.sky,(0,0))
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
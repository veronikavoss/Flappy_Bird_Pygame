from setting import *
from player import Player
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
    
    def update(self):
        self.player.update()
    
    def draw(self):
        self.screen.blit(self.sky,(0,0))
        self.player.draw(self.screen)
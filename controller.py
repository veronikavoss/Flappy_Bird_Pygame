from setting import *
from player import Player
from ground import Ground
from ui import Ui
import random


class Controller:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        
        self.set_sky_image()
        self.ground=pygame.sprite.GroupSingle(Ground(self.asset))
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
        self.ui=Ui(self.asset)
    
    def set_sky_image(self):
        sky=random.choice(list(self.asset.stage_images['sky'].keys()))
        self.sky_image=self.asset.stage_images['sky'][sky]
    
    def update(self):
        self.ground.update()
        self.player.update()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.sky_image,(0,0))
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
        self.ui.draw(self.screen)
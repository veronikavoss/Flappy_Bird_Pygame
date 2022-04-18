from setting import *
from player import Player

class Controller:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
    
    def update(self):
        self.player.update()
    
    def draw(self):
        self.player.draw(self.screen)
import numbers
from setting import *

class Ui:
    def __init__(self,asset):
        self.asset=asset
        
        self.start_screen_images()
        self.number_images()
    
    def start_screen_images(self):
        self.logo=self.asset.start_screen['logo']
        self.logo_rect=self.logo.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//4))
        
        self.play_button=self.asset.start_screen['play_button']
        self.start_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SKY_HEIGHT//1.5))
        self.game_over_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SKY_HEIGHT//1.5))
        
        self.ranking=self.asset.start_screen['ranking']
        self.ranking_rect=self.ranking.get_rect(center=(SKY_WIDTH-(SKY_WIDTH//3.6),SKY_HEIGHT//1.5))
    
    def number_images(self):
        number=9
        self.large_numbers=self.asset.number_images['large'][number]
        self.large_number_rect=self.large_numbers.get_rect()
        
        self.medium_numbers=self.asset.number_images['medium'][number]
        self.medium_number_rect=self.medium_numbers.get_rect()
        
        self.small_numbers=self.asset.number_images['small'][number]
        self.small_number_rect=self.small_numbers.get_rect()
    
    def draw(self,screen):
        screen.blits([
            # [self.large_numbers,self.large_number_rect],
            # [self.medium_numbers,self.medium_number_rect],
            # [self.small_numbers,self.small_number_rect],
            [self.logo,self.logo_rect],
            [self.play_button,self.start_play_button_rect],
            [self.ranking,self.ranking_rect]
        ])
from setting import *

class Ui:
    def __init__(self,asset):
        self.asset=asset
        
        self.start_screen_images()
        # self.number_images()
    
    def start_screen_images(self):
        self.logo=self.asset.start_screen['logo']
        self.logo_rect=self.logo.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//4))
        
        self.play_button=self.asset.start_screen['play_button']
        self.start_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SKY_HEIGHT//1.5))
        self.game_over_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SKY_HEIGHT//1.5))
        
        self.ranking=self.asset.start_screen['ranking']
        self.ranking_rect=self.ranking.get_rect(center=(SKY_WIDTH-(SKY_WIDTH//3.6),SKY_HEIGHT//1.5))
    
    def get_number_images_size(self,size):
        number=self.asset.number_images[size][0]
        self.number_width=number.get_size()[0]
        return self.number_width
    
    def start_screen_draw(self,screen):
        screen.blits([
            [self.logo,self.logo_rect],
            [self.play_button,self.start_play_button_rect],
            [self.ranking,self.ranking_rect]
        ])
    
    def score_draw(self,screen,score):
        for idx,number in enumerate(reversed(list(str(score)))):
            if idx==0:
                pos_x=SKY_WIDTH//2+(self.get_number_images_size('large')//2*(len(str(score))-1))
            elif idx==1:
                pos_x=(SKY_WIDTH//2-self.get_number_images_size('large'))+(self.get_number_images_size('large')//2*(len(str(score))-1))
            elif idx==2:
                pos_x=(SKY_WIDTH//2-self.get_number_images_size('large')*2)+(self.get_number_images_size('large')//2*(len(str(score))-1))
            elif idx==3:
                pos_x=(SKY_WIDTH//2-self.get_number_images_size('large')*3)+(self.get_number_images_size('large')//2*(len(str(score))-1))
            
            large_number=self.asset.number_images['large'][int(number)]
            large_number_rect=large_number.get_rect(center=(pos_x,SKY_HEIGHT//6))
            screen.blit(large_number,large_number_rect)
#%%
for i,j in enumerate('100'):
    print(i,j)
#%%

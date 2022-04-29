from setting import *

class Ui:
    def __init__(self,asset):
        self.asset=asset
        
        self.set_ui_images()
    
    def set_ui_images(self):
        self.logo_image=self.asset.ui_images['logo']
        self.logo_image_rect=self.logo_image.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//3))
        
        self.play_button=self.asset.ui_images['play_button']
        self.start_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SCREEN_HEIGHT//1.5))
        self.game_over_play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SKY_HEIGHT//1.5))
        
        self.ranking_button=self.asset.ui_images['ranking_button']
        self.ranking_button_rect=self.ranking_button.get_rect(center=(SKY_WIDTH-(SKY_WIDTH//3.6),SCREEN_HEIGHT//1.5))
        
        self.ready_image=self.asset.ui_images['ready']
        self.ready_image_rect=self.ready_image.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//3))
        
        self.tap_image=self.asset.ui_images['tap']
        self.tap_image_rect=self.tap_image.get_rect(center=(SKY_WIDTH//2,SCREEN_HEIGHT//1.6))
        self.tap_image_y=self.tap_image_rect.y
        
        self.game_over_image=self.asset.ui_images['game_over']
        self.game_over_image_rect=self.game_over_image.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//6))
        
        self.score_board_image=self.asset.ui_images['score_board']
        self.score_board_image_rect=self.score_board_image.get_rect(centerx=SCREEN_WIDTH//2,bottom=SCREEN_HEIGHT//2)
        
        self.new_image=self.asset.ui_images['new']
        self.new_image_rect=self.new_image.get_rect(center=(SCREEN_WIDTH/1.6,SKY_HEIGHT/1.94))
        
        self.medal=0
        self.medal_image=self.asset.ui_images['medal'][self.medal]
        self.medal_image_rect=self.medal_image.get_rect(center=(SCREEN_WIDTH/3.6,SKY_HEIGHT/1.9))
    
    def draw_start_screen(self,screen):
        if self.player.sprite.game_status=='start_screen':
            screen.blits([
                [self.logo_image,self.logo_image_rect],
                [self.play_button,self.start_play_button_rect],
                [self.ranking_button,self.ranking_button_rect]
            ])
    
    def tap_image_animate(self):
        if self.player.sprite.game_status=='ready_screen':
            if pygame.time.get_ticks()//800%2==0:
                self.tap_image_rect.y=self.tap_image_y-2*SCALE
            else:
                self.tap_image_rect.y=self.tap_image_y+2*SCALE
    
    def draw_ready_screen(self,screen):
        if self.player.sprite.game_status=='ready_screen':
            screen.blits([
                [self.ready_image,self.ready_image_rect],
                [self.tap_image,self.tap_image_rect]
            ])
    
    def get_number_images_size(self,size):
        number=self.asset.number_images[size][0]
        self.number_width=number.get_size()[0]
        return self.number_width
    
    def draw_score(self,screen,score):
        if self.player.sprite.game_status!='start_screen' and self.player.sprite.game_status!='game_over_screen':
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
                large_number_rect=large_number.get_rect(center=(pos_x,SKY_HEIGHT//8))
                screen.blit(large_number,large_number_rect)
        elif self.player.sprite.game_status=='game_over_screen':
            pass
    
    def draw_game_over(self,screen,score):
        if self.player.sprite.game_status=='game_over_screen':
            screen.blits([
                [self.game_over_image,self.game_over_image_rect],
                [self.score_board_image,self.score_board_image_rect],
                [self.new_image,self.new_image_rect]
            ])
            self.medal=max(0,4-score//10)
            if 0<=self.medal<=3:
                self.medal_image=self.asset.ui_images['medal'][self.medal]
                screen.blit(self.medal_image,self.medal_image_rect)
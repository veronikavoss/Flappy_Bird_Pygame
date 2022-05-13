from setting import *

class Ui:
    def __init__(self,asset):
        self.asset=asset
        
        self.set_ui_images()
    
    def set_ui_images(self):
        self.logo_image=self.asset.ui_images['logo']
        self.logo_image_rect=self.logo_image.get_rect(center=(SKY_WIDTH//2,SKY_HEIGHT//3))
        
        self.play_button=self.asset.ui_images['play_button']
        self.play_button_rect=self.play_button.get_rect(center=(SKY_WIDTH//3.6,SCREEN_HEIGHT//1.5))
        
        self.ranking_button=self.asset.ui_images['ranking_button']
        self.ranking_button_rect=self.ranking_button.get_rect(center=(SKY_WIDTH-(SKY_WIDTH//3.6),SCREEN_HEIGHT//1.5))
        
        self.back_button=self.asset.ui_images['back_button']
        self.back_button_rect=self.back_button.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.2))
            
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
        self.new_image_rect=self.new_image.get_rect(center=(SCREEN_WIDTH/1.6,SKY_HEIGHT/1.93))
        
        self.medal=0
        self.medal_image=self.asset.ui_images['medal'][self.medal]
        self.medal_image_rect=self.medal_image.get_rect(center=(SCREEN_WIDTH/3.6,SKY_HEIGHT/1.9))
    
    def draw_start_screen(self):
        if self.player.sprite.game_status=='start_screen':
            self.screen.blits([
                [self.logo_image,self.logo_image_rect],
                [self.play_button,self.play_button_rect],
                [self.ranking_button,self.ranking_button_rect]
            ])
    
    def tap_image_animate(self):
        if self.player.sprite.game_status=='ready_screen':
            if pygame.time.get_ticks()//800%2==0:
                self.tap_image_rect.y=self.tap_image_y-2*SCALE
            else:
                self.tap_image_rect.y=self.tap_image_y+2*SCALE
    
    def draw_ready_screen(self):
        if self.player.sprite.game_status=='ready_screen':
            self.screen.blits([
                [self.ready_image,self.ready_image_rect],
                [self.tap_image,self.tap_image_rect]
            ])
    
    def get_number_images_size(self,size):
        number=self.asset.number_images[size][0]
        self.number_width=number.get_size()[0]
        return self.number_width
    
    def draw_game_over(self):
        if self.player.sprite.game_status=='game_over_screen':
            if self.score>self.high_score and not self.best_score:
                self.save_high_score()
                self.open_high_score()
                self.best_score=True
            
            self.screen.blits([
                [self.game_over_image,self.game_over_image_rect],
                [self.score_board_image,self.score_board_image_rect],
                [self.play_button,self.play_button_rect],
                [self.ranking_button,self.ranking_button_rect]
            ])
            self.medal=max(0,4-self.score//10)
            if 0<=self.medal<=3:
                self.medal_image=self.asset.ui_images['medal'][self.medal]
                self.screen.blit(self.medal_image,self.medal_image_rect)
            
            if self.best_score:
                self.screen.blit(self.new_image,self.new_image_rect)
    
    def draw_score(self):
        # main_score
        if self.player.sprite.game_status!='start_screen' and \
            self.player.sprite.game_status!='game_over_screen' and \
                self.player.sprite.game_status!='rank_screen':
            size='large'
            for idx,number in enumerate(reversed(list(str(self.score)))):
                if idx==0:
                    pos_x=SKY_WIDTH//2+(self.get_number_images_size(size)//2*(len(str(self.score))-1))
                elif idx==1:
                    pos_x=(SKY_WIDTH//2-self.get_number_images_size(size))+(self.get_number_images_size(size)//2*(len(str(self.score))-1))
                elif idx==2:
                    pos_x=(SKY_WIDTH//2-self.get_number_images_size(size)*2)+(self.get_number_images_size(size)//2*(len(str(self.score))-1))
                elif idx==3:
                    pos_x=(SKY_WIDTH//2-self.get_number_images_size(size)*3)+(self.get_number_images_size(size)//2*(len(str(self.score))-1))
                number_image=self.asset.number_images[size][int(number)]
                number_image_rect=number_image.get_rect(center=(pos_x,SKY_HEIGHT//8))
                self.screen.blit(number_image,number_image_rect)
            
        # result_score
        elif self.player.sprite.game_status=='game_over_screen':
            size='medium'
            # current_score
            for idx,number in enumerate(reversed(list(str(self.score)))):
                if idx==0:
                    pos_x=SKY_WIDTH/1.26
                elif idx==1:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size))
                elif idx==2:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size)*2)
                elif idx==3:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size)*3)
                number_image=self.asset.number_images[size][int(number)]
                number_image_rect=number_image.get_rect(center=(pos_x,SKY_HEIGHT/2.15))
                self.screen.blit(number_image,number_image_rect)
            
            # best_score
            for idx,number in enumerate(reversed(list(str(self.high_score)))):
                if idx==0:
                    pos_x=SKY_WIDTH/1.26
                elif idx==1:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size))
                elif idx==2:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size)*2)
                elif idx==3:
                    pos_x=(SKY_WIDTH/1.26-self.get_number_images_size(size)*3)
                number_image=self.asset.number_images[size][int(number)]
                number_image_rect=number_image.get_rect(center=(pos_x,SKY_HEIGHT/1.75))
                self.screen.blit(number_image,number_image_rect)
    
    def draw_rank(self):
        if self.player.sprite.game_status=='rank_screen':
            # rank_background
            surface=pygame.Surface(SCREEN_SIZE)
            surface.fill('black')
            surface.set_alpha(128)
            
            # ranking_text
            ranking=self.asset.ranking_font.render('RANKING',True,'green')
            ranking_rect=ranking.get_rect(centerx=SCREEN_WIDTH//2,y=20)
            
            self.screen.blits([[surface,(0,0)],[ranking,ranking_rect],[self.back_button,self.back_button_rect]])
            
            # high_score_ranking
            if self.open_high_score():
                for idx,score in enumerate(self.open_high_score()[0:15]):
                    rank=self.asset.high_score_font.render(f'{idx+1}.  {score[0]} pts  {score[1]}, {score[2]}',True,'white')
                    y=idx*(rank.get_height()+rank.get_height()/2)+70
                    rank_rect=rank.get_rect(x=SCREEN_WIDTH/6,y=y)
                    self.screen.blit(rank,rank_rect)
            else:
                rank=self.asset.high_score_font.render('No Result',True,'white')
                rank_rect=rank.get_rect(centerx=SCREEN_WIDTH/2,y=70)
                self.screen.blit(rank,rank_rect)
from setting import *

class Asset:
    def __init__(self):
        self.icon_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'icon.png')).convert_alpha()
        self.general_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'General.png')).convert_alpha()
        
        self.get_ui_images()
        self.get_number_images()
        self.get_stage_images()
        self.get_player_images()
        self.get_pipe_images()
        self.get_sounds()
        self.set_font()
    
    def get_ui_images(self):
        self.title_icon=pygame.Surface((29,29))
        self.title_icon.blit(self.icon_sheet_image,(0,0),(592,0,29,29))
        
        self.ui_images={'logo':None,'play_button':None,'ranking_button':None,'back_button':None,
                        'ready':None,'tap':None,
                        'game_over':None,'score_board':None,'new':None,'medal':[]}
        
        logo_img=pygame.Surface((89,24))
        logo_img.blit(self.general_sheet_image,(0,0),(351,91,89,24))
        logo_img.set_colorkey((0,0,0))
        logo_img=pygame.transform.scale(logo_img,(89*SCALE,24*SCALE))
        self.ui_images['logo']=logo_img
        
        play_button_img=pygame.Surface((52,29))
        play_button_img.blit(self.general_sheet_image,(0,0),(354,118,52,29))
        play_button_img.set_colorkey((0,0,0))
        play_button_img=pygame.transform.scale(play_button_img,(52*SCALE,29*SCALE))
        self.ui_images['play_button']=play_button_img
        
        ranking_img=pygame.Surface((52,29))
        ranking_img.blit(self.general_sheet_image,(0,0),(414,118,52,29))
        ranking_img.set_colorkey((0,0,0))
        ranking_img=pygame.transform.scale(ranking_img,(52*SCALE,29*SCALE))
        self.ui_images['ranking_button']=ranking_img
        
        back_button=pygame.Surface((40,14))
        back_button.blit(self.general_sheet_image,(0,0),(462,42,40,14))
        back_button=pygame.transform.scale(back_button,(40*SCALE,14*SCALE))
        self.ui_images['back_button']=back_button
        
        ready_img=pygame.Surface((92,25))
        ready_img.blit(self.general_sheet_image,(0,0),(295,59,92,25))
        ready_img.set_colorkey((0,0,0))
        ready_img=pygame.transform.scale(ready_img,(92*SCALE,25*SCALE))
        self.ui_images['ready']=ready_img
        
        tap_img=pygame.Surface((57,49))
        tap_img.blit(self.general_sheet_image,(0,0),(292,91,57,49))
        tap_img.set_colorkey((0,0,0))
        tap_img=pygame.transform.scale(tap_img,(57*SCALE,49*SCALE))
        self.ui_images['tap']=tap_img
        
        game_over_img=pygame.Surface((96,21))
        game_over_img.blit(self.general_sheet_image,(0,0),(395,59,96,21))
        game_over_img.set_colorkey((0,0,0))
        game_over_img=pygame.transform.scale(game_over_img,(96*SCALE,21*SCALE))
        self.ui_images['game_over']=game_over_img
        
        score_board_img=pygame.Surface((113,57))
        score_board_img.blit(self.general_sheet_image,(0,0),(3,259,113,57))
        score_board_img.set_colorkey((0,0,0))
        score_board_img=pygame.transform.scale(score_board_img,(113*SCALE,57*SCALE))
        self.ui_images['score_board']=score_board_img
        
        new_img=pygame.Surface((16,7))
        new_img.blit(self.general_sheet_image,(0,0),(112,501,16,7))
        new_img.set_colorkey((0,0,0))
        new_img=pygame.transform.scale(new_img,(16*SCALE,7*SCALE))
        self.ui_images['new']=new_img
        
        medal_pos=[[121,258,22,22],[121,282,22,22],[112,453,22,22],[112,477,22,22]]
        for pos in medal_pos:
            surface=pygame.Surface((22,22))
            surface.blit(self.general_sheet_image,(0,0),pos)
            surface.set_colorkey((0,0,0))
            surface=pygame.transform.scale(surface,(22*SCALE,22*SCALE))
            self.ui_images['medal'].append(surface)
    
    def get_number_images(self):
        self.number_images={'large':[],'medium':[],'small':[]}
        
        # large number
        large_number_offset=[[496,60,12,18],[134,455,12,18]]
        for rect in large_number_offset:
            surface=pygame.Surface((12,18))
            surface.blit(self.general_sheet_image,(0,0),rect)
            surface.set_colorkey((0,0,0))
            surface=pygame.transform.scale(surface,(12*SCALE,18*SCALE))
            self.number_images['large'].append(surface)
        
        for y in range(2):
            for x in range(4):
                surface=pygame.Surface((12,18))
                surface.blit(self.general_sheet_image,(0,0),(292+x*14,160+y*24,12,18))
                surface.set_colorkey((0,0,0))
                surface=pygame.transform.scale(surface,(12*SCALE,18*SCALE))
                self.number_images['large'].append(surface)
        
        # medium number
        medium_number_offset=[
            [137,306,7,10],[137,477,7,10],[137,489,7,10],[131,501,7,10],[502,0,7,10],\
            [502,12,7,10],[505,26,7,10],[505,42,7,10],[293,242,7,10],[311,206,7,10]]
        for rect in medium_number_offset:
            surface=pygame.Surface((7,10))
            surface.blit(self.general_sheet_image,(0,0),rect)
            surface.set_colorkey((0,0,0))
            surface=pygame.transform.scale(surface,(7*SCALE,10*SCALE))
            self.number_images['medium'].append(surface)
        
        # small number
        for i in range(5):
            for j in range(2):
                y=j*9
                surface=pygame.Surface((6,7))
                surface.blit(self.general_sheet_image,(0,0),(138,323+(i*26)+y,6,7))
                surface.set_colorkey((0,0,0))
                surface=pygame.transform.scale(surface,(6*SCALE,7*SCALE))
                self.number_images['small'].append(surface)
    
    def get_stage_images(self):
        sky_size=144,256
        ground_size=168,56
        self.stage_images={'sky':{'day':None,'night':None},'ground':None}
        
        for i,sky in enumerate(self.stage_images['sky'].keys()):
            surface=pygame.Surface(sky_size)
            surface.blit(self.general_sheet_image,(0,0),(146*i,0,144,256))
            surface=pygame.transform.scale(surface,SCREEN_SIZE)
            self.stage_images['sky'][sky]=surface
        
        self.stage_images['ground']=pygame.Surface(ground_size)
        self.stage_images['ground'].blit(self.general_sheet_image,(0,0),(292,0,168,56))
        self.stage_images['ground']=pygame.transform.scale(self.stage_images['ground'],GROUND_SIZE)
    
    def get_player_images(self):
        self.player_images={'yellow':[],'blue':[],'red':[]}
        
        player_images_offset=[
            [[3,491,17,12],[31,491,17,12],[59,491,17,12]],
            [[87,491,17,12],[115,329,17,12],[115,355,17,12]],
            [[115,381,17,12],[115,407,17,12],[115,433,17,12]]
        ]
        
        for i,color in enumerate(self.player_images.keys()):
            for rect in player_images_offset[i]:
                surface=pygame.Surface((17,12))
                surface.blit(self.general_sheet_image,(0,0),rect)
                surface.set_colorkey((0,0,0))
                surface=pygame.transform.scale(surface,PLAYER_SIZE)
                self.player_images[color].append(surface)
    
    def get_pipe_images(self):
        self.pipe_images={'red':None,'green':None}
        
        pipe_images_offset=[[0,323,26,160],[84,323,26,160]]
        
        for idx,pipe in enumerate(pipe_images_offset):
            surface=pygame.Surface((26,160))
            surface.blit(self.general_sheet_image,(0,0),pipe)
            surface.set_colorkey((0,0,0))
            surface=pygame.transform.scale(surface,(26*SCALE,160*SCALE))
            if idx==0:
                self.pipe_images['red']=surface 
            else:
                self.pipe_images['green']=surface
    
    def get_sounds(self):
        self.swooshing_sound=pygame.mixer.Sound(os.path.join(SOUND_PATH,'sfx_swooshing.wav'))
        self.swooshing_sound.set_volume(VOLUME*0.01)
        self.die_sound=pygame.mixer.Sound(os.path.join(SOUND_PATH,'sfx_die.wav'))
        self.die_sound.set_volume(VOLUME*0.01)
        self.point_sound=pygame.mixer.Sound(os.path.join(SOUND_PATH,'sfx_point.wav'))
        self.point_sound.set_volume(VOLUME*0.01)
        self.wing_sound=pygame.mixer.Sound(os.path.join(SOUND_PATH,'sfx_wing.wav'))
        self.wing_sound.set_volume(VOLUME*0.01)
        self.crash_sound=pygame.mixer.Sound(os.path.join(SOUND_PATH,'sfx_hit.wav'))
        self.crash_sound.set_volume(VOLUME*0.01)
    
    def set_font(self):
        self.font=pygame.font.SysFont(None,32)
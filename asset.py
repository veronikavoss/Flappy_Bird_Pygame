from setting import *

class Asset:
    def __init__(self):
        self.icon_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'icon.png')).convert_alpha()
        self.general_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'General.png')).convert_alpha()
        
        self.get_ui_image()
        self.get_number_image()
        self.get_stage_image()
        self.get_player_image()
    
    def get_ui_image(self):
        self.title_icon=pygame.Surface((29,29))
        self.title_icon.blit(self.icon_sheet_image,(0,0),(592,0,29,29))
        
        self.start_screen={'logo':None,'play_button':None,'ranking_button':None,'ready':None,'tap':None}
        
        logo_img=pygame.Surface((89,24))
        logo_img.blit(self.general_sheet_image,(0,0),(351,91,89,24))
        logo_img.set_colorkey((0,0,0))
        logo_img=pygame.transform.scale(logo_img,(89*SCALE,24*SCALE))
        self.start_screen['logo']=logo_img
        
        play_button_img=pygame.Surface((52,29))
        play_button_img.blit(self.general_sheet_image,(0,0),(354,118,52,29))
        play_button_img.set_colorkey((0,0,0))
        play_button_img=pygame.transform.scale(play_button_img,(52*SCALE,29*SCALE))
        self.start_screen['play_button']=play_button_img
        
        ranking_img=pygame.Surface((52,29))
        ranking_img.blit(self.general_sheet_image,(0,0),(414,118,52,29))
        ranking_img.set_colorkey((0,0,0))
        ranking_img=pygame.transform.scale(ranking_img,(52*SCALE,29*SCALE))
        self.start_screen['ranking_button']=ranking_img
        
        ready_img=pygame.Surface((92,25))
        ready_img.blit(self.general_sheet_image,(0,0),(295,59,92,25))
        ready_img.set_colorkey((0,0,0))
        ready_img=pygame.transform.scale(ready_img,(92*SCALE,25*SCALE))
        self.start_screen['ready']=ready_img
        
        tap_img=pygame.Surface((57,49))
        tap_img.blit(self.general_sheet_image,(0,0),(292,91,57,49))
        tap_img.set_colorkey((0,0,0))
        tap_img=pygame.transform.scale(tap_img,(57*SCALE,49*SCALE))
        self.start_screen['tap']=tap_img
    
    def get_number_image(self):
        self.number_images={'large':[],'medium':[],'small':[]}
        
        # large number
        large_number_pos=[[496,60,12,18],[136,455,12,18]]
        for rect in large_number_pos:
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
        medium_number_pos=[
            [137,306,7,10],[137,477,7,10],[137,489,7,10],[131,501,7,10],[502,0,7,10],\
            [502,12,7,10],[505,26,7,10],[505,42,7,10],[293,242,7,10],[311,206,7,10]]
        for rect in medium_number_pos:
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
    
    def get_stage_image(self):
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
    
    def get_player_image(self):
        self.player_images={'yellow':[],'blue':[],'red':[]}
        positions=[
            [[3,491,17,12],[31,491,17,12],[59,491,17,12]],
            [[87,491,17,12],[115,329,17,12],[115,355,17,12]],
            [[115,381,17,12],[115,407,17,12],[115,433,17,12]]
        ]
        
        for i,color in enumerate(self.player_images.keys()):
            for rect in positions[i]:
                surface=pygame.Surface((17,12))
                surface.blit(self.general_sheet_image,(0,0),rect)
                surface.set_colorkey((0,0,0))
                surface=pygame.transform.scale(surface,PLAYER_SIZE)
                self.player_images[color].append(surface)

# Asset()
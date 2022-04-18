from setting import *

class Asset:
    def __init__(self):
        self.icon_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'icon.png')).convert_alpha()
        self.general_sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'General.png')).convert_alpha()
        
        self.get_ui_image()
        self.get_stage_image()
        self.get_player_image()
    
    def get_ui_image(self):
        self.title_icon=pygame.Surface((29,29))
        self.title_icon.blit(self.icon_sheet_image,(0,0),(592,0,29,29))
    
    def get_stage_image(self):
        sky_size=144,256
        ground_size=168,56
        self.stage_images={'sky':{'day':None,'night':None},'ground':None}
        
        for i,sky in enumerate(self.stage_images['sky'].keys()):
            surface=pygame.Surface(sky_size)
            surface.blit(self.general_sheet_image,(0,0),(146*i,0,144,256))
            surface=pygame.transform.scale(surface,SKY_SIZE)
            self.stage_images['sky'][sky]=surface
        
        self.stage_images['ground']=pygame.Surface(ground_size)
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
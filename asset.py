from setting import *

class Asset:
    def __init__(self):
        self.sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'General.png')).convert_alpha()
        
        self.get_player_image()
    
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
                surface.blit(self.sheet_image,(0,0),rect)
                surface.set_colorkey((0,0,0))
                surface=pygame.transform.scale(surface,PLAYER_SIZE)
                self.player_images[color].append(surface)
from asset import Asset
from setting import *
from controller import Controller

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        self.asset=Asset()
        self.clock=pygame.time.Clock()
        self.start()
    
    def start(self):
        self.controller=Controller(self.screen,self.asset)
        self.loop()
    
    def loop(self):
        self.playing=True
        while self.playing:
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.screen.fill('white')
        self.controller.draw()

if __name__=='__main__':
    Main()
    pygame.quit()
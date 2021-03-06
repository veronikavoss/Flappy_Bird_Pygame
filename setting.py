import pygame,os

CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH=os.path.join(CURRENT_PATH,'image')
SOUND_PATH=os.path.join(CURRENT_PATH,'sound')

TITLE='Flappy Bird'
SCALE=3
FPS=60
VOLUME=50

GROUND_SIZE=GROUND_WIDTH,GROUND_HEIGHT=168*SCALE,56*SCALE
SKY_SIZE=SKY_WIDTH,SKY_HEIGHT=144*SCALE,256*SCALE-GROUND_HEIGHT
SCREEN_SIZE=SCREEN_WIDTH,SCREEN_HEIGHT=SKY_WIDTH,256*SCALE
PLAYER_SIZE=PLAYER_WIDTH,PLAYER_HEIGHT=17*SCALE,12*SCALE
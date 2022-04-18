import pygame,os

TITLE='Flappy Bird'
SCALE=3
SKY_SIZE=SKY_WIDTH,SKY_HEIGHT=144*SCALE,256*SCALE
GROUND_SIZE=GROUND_WIDTH,GROUND_HEIGHT=168*SCALE,56*SCALE
SCREEN_SIZE=SCREEN_WIDTH,SCREEN_HEIGHT=SKY_WIDTH,(SKY_HEIGHT+GROUND_HEIGHT)
PLAYER_SIZE=PLAYER_WIDTH,PLAYER_HEIGHT=17*SCALE,12*SCALE
FPS=60

CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH=os.path.join(CURRENT_PATH,'image')
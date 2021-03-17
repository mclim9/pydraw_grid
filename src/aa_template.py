"""Create Grid of Objects"""
import pygame
import random
from colors import c
from pygame.locals import QUIT
from pygame import gfxdraw
from math   import pi

WHITE = c().WHITE
BLACK = c().BLACK

################################################################################
### Definitions
################################################################################
class widget:
    ###Class to keep track of a each squarewidget_ plot
    def __init__(self,xPos,yPos,Size):
        self.color      = random.choice(c().Colors)
        self.x          = int(xPos)
        self.y          = int(yPos)
        self.size       = Size

    def draw(self, screen):
        self.screen = screen
        self.draw_widget()

    def draw_widget(self):
        rectX = int(self.x - self.size/2)       # Upper Left X
        rectY = int(self.y - self.size/2)       # Upper Left Y
        pygame.draw.rect(self.screen, self.color , (rectX,rectY,self.size,self.size), 0)    # Square
        pygame.draw.rect(self.screen, WHITE      , (rectX,rectY,self.size,self.size), 1)    # Frame

if __name__ == "__main__":
    widget_Size  = 100
    pygame.init()
    screen = pygame.display.set_mode([widget_Size, widget_Size])
    widget_ = widget(widget_Size/2, widget_Size/2, widget_Size)
    widget_.draw(screen)
    pygame.display.update()                     # update the screen
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()

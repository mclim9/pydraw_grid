################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Square Smiles
###
################################################################################
### User Inputs
################################################################################
squaresX  = 6
squaresY  = 6
lineLen  = 5
glyphSize   = (squaresX + 2) * lineLen
################################################################################
### Code Begin
################################################################################
numCol      = 10
numRow      = 10
ScrWid      = (numCol + 2) * glyphSize
ScrHeight   = (numRow + 2) * glyphSize

import pygame
import random
import math
import time
from colors import c
from pygame import gfxdraw
from math   import pi
WHITE = c().WHITE
BLACK = c().BLACK

################################################################################
### Define colors
################################################################################

from pygame.locals import DOUBLEBUF, FULLSCREEN
flags = DOUBLEBUF       # FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Definitions
################################################################################
class glyph:
    ###Class to keep track of a each glyph plot
    def __init__(self,xPos,yPos,Size):
        self.size       = Size
        self.color      = random.choice(c().Muted)
        # self.color      = WHITE
        self.x          = int(xPos)
        self.y          = int(yPos)
        self.Xorigin    = int(self.x - self.size/2)
        self.Yorigin    = int(self.y - self.size/2)
        self.squaresX = 6
        self.squaresY = 6
        self.segments   = []
        self.symmetryV  = 1

        numI = int(self.squaresX/2) if self.symmetryV else self.squaresX
        for i in range(numI):
            for j in range(squaresY):
                UpRti = self.Xorigin + (i+1) * lineLen
                UpRtj = self.Yorigin + (j+1) * lineLen
                UpLti = self.Xorigin + (self.squaresX - i) * lineLen
                UpRtj = self.Yorigin + (j+1) * lineLen
                if random.randint(0,100) < 50:      #Hori Line
                    self.segments.append([(UpRti,UpRtj),(UpRti+lineLen,UpRtj)])
                    if self.symmetryV: self.segments.append([(UpLti,UpRtj),(UpLti-lineLen,UpRtj)])
                if random.randint(0,100) < 65:      #Vert Line
                    self.segments.append([(UpRti,UpRtj),(UpRti,UpRtj+lineLen)])
                    if self.symmetryV: self.segments.append([(UpLti,UpRtj),(UpLti,UpRtj+lineLen)])
                # if random.randint(0,200) < 1:      #Diag Line
                #     self.segments.append([(UpRti,UpRtj),(UpRti+lineLen,UpRtj+lineLen)])
                #     self.segments.append([(UpLti,UpRtj),(UpLti-lineLen,UpRtj+lineLen)])
                # if random.randint(0,100) < 5:      #Diag Line
                #     self.segments.append([(UpRti+lineLen,UpRtj),(UpRti,UpRtj+lineLen)])

    def draw(self, screen):
        self.screen = screen
        self.draw_bkgnd()
        for points in self.segments:
            pygame.draw.lines(self.screen, BLACK, False, points, 3)

    def draw_bkgnd(self):
        pygame.draw.rect(self.screen, self.color , (self.Xorigin,self.Yorigin,self.size,self.size), 0)
        pygame.draw.rect(self.screen, WHITE      , (self.Xorigin,self.Yorigin,self.size,self.size), 1)

def makeGlyph(self):
    print('Hello')

################################################################################
### Main Code
################################################################################
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [ScrWid, ScrHeight]
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)

    pygame.display.set_caption("glyph Plot")
    done                    = False
    clock = pygame.time.Clock()     # Manage screen updates

    ###########################################################################
    ### Main Code
    ###########################################################################
    while not done:
        glyphArry = []
        for i in range(numCol):
            for j in range(numRow):
                xPos = int((i+1) * glyphSize + glyphSize/2)
                yPos = int((j+1) * glyphSize + glyphSize/2)
                glyphArry.append(glyph(xPos,yPos,glyphSize))

        #######################################################################
        ### Event Processing
        #######################################################################
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #######################################################################
        ### Drawing Code
        #######################################################################
        screen.fill(WHITE)              # Set the screen background
        for face in glyphArry:
            face.draw(screen)
        clock.tick(0.5)                 # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    pygame.image.save(screen, f"Glyph_{numCol}x{numRow}_{glyphSize}x{face.squaresX}x{squaresY}_SymV{face.symmetryV}.jpg")
    # var = input("Please enter something: ")

if __name__ == "__main__":
    main()

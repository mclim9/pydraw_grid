"""Create Grid of Objects"""
CellSize  = 100

################################################################################
### Code Begin
################################################################################
numCol      = 5
numRow      = 5
ScrWid      = (numCol+2) * CellSize
ScrHeight   = (numRow+2) * CellSize

import pygame
import random
import time
# from Face   import squareFace as Cell
from aa_template   import widget as Cell
# from Glyphs import glyph as Cell
from colors import c
WHITE = c().WHITE
BLACK = c().BLACK

################################################################################
### Define colors
################################################################################
from pygame.locals import DOUBLEBUF, FULLSCREEN
flags = pygame.locals.DOUBLEBUF       # FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Main Code
################################################################################
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [ScrWid, ScrHeight]
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)

    pygame.display.set_caption("pyDraw Grid")
    done                    = False
    clock = pygame.time.Clock()     # Manage screen updates

    ###########################################################################
    ### Main Code
    ###########################################################################
    while not done:
        CellArray = []
        for i in range(numCol):
            for j in range(numRow):
                xPos = int((i+1) * CellSize + CellSize/2)
                yPos = int((j+1) * CellSize + CellSize/2)
                CellArray.append(Cell(xPos,yPos,CellSize))

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
        screen.fill(BLACK)              # Set the screen background
        for face in CellArray:
            face.draw(screen)
        clock.tick(0.5)                 # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While

if __name__ == "__main__":
    main()

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
class squareFace:
    ###Class to keep track of a each squareFace plot
    def __init__(self,xPos,yPos,Size):
        self.Eyes       = ['Open','Wow','Small']
        self.Pupils     = [0.3,0.5,0.5,0.9,0.5]
        self.size       = Size
        self.color      = random.choice(c().Colors)
        self.x          = int(xPos)
        self.y          = int(yPos)
        self.eyeType    = random.choice(self.Eyes)
        self.eyeSize    = int(self.size/10)
        self.eyePupil   = int(self.eyeSize*random.choice(self.Pupils))
        if self.size < 20:
            self.eyeType    = 'Small'
            self.eyeSize    = 1
            self.eyePupil   = 1

    def draw(self, screen):
        self.screen = screen
        self.draw_face()
        self.draw_eyes()
        self.draw_mouth()

    def draw_face(self):
        rectX = int(self.x - self.size/2)
        rectY = int(self.y - self.size/2)
        pygame.draw.rect(self.screen, self.color , (rectX,rectY,self.size,self.size), 0)
        pygame.draw.rect(self.screen, WHITE      , (rectX,rectY,self.size,self.size), 1)

    def draw_eyes(self):
        eyeOffX = int(self.size/5)
        if random.randint(0,100) > 1:
            """Draw eyes w/ pupil"""
            self.draw_eyeCircle(self.x + eyeOffX, self.y, self.eyeSize,  WHITE)
            self.draw_eyeCircle(self.x - eyeOffX, self.y, self.eyeSize,  WHITE)
            self.draw_eyeCircle(self.x + eyeOffX, self.y, self.eyePupil, BLACK)
            self.draw_eyeCircle(self.x - eyeOffX, self.y, self.eyePupil, BLACK)
        else:
            """Draw eyes closed"""
            pygame.draw.aaline(self.screen, BLACK, (self.x - eyeOffX - self.eyeSize, self.y), (self.x - eyeOffX + self.eyeSize, self.y), 1)
            pygame.draw.aaline(self.screen, BLACK, (self.x + eyeOffX + self.eyeSize, self.y), (self.x + eyeOffX - self.eyeSize, self.y), 1)

    def draw_eyeCircle(self, x, y, radius, color):
        if radius > 1:
            pygame.gfxdraw.filled_circle(self.screen, x, y, radius, color)      #Draw filled in circle
        pygame.gfxdraw.aacircle(self.screen, x, y, radius, color)           #AntiAlias edge

    def draw_mouth(self):
        mouthArry = ['open','line','smile','dot','open','line','smile','open','line','smile','dot']
        mouth = random.choice(mouthArry)
        mouthSize = int(self.size/20)
        if self.size < 20:
            mouthSize = 2
            mouth     = 'dot'
        if mouth == 'open':
            mouthOff = int(self.size/5)
            pygame.gfxdraw.filled_circle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
            pygame.gfxdraw.aacircle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
        elif mouth == 'line':
            mouthOff = int(self.size/5)
            pygame.draw.aaline(self.screen, BLACK,(self.x-mouthSize,self.y+mouthOff),(self.x+mouthSize,self.y+mouthOff))
        elif mouth == 'smile':
            mouthOff = int(self.size/10)
            pygame.draw.arc(self.screen, BLACK,[self.x-mouthSize, self.y+mouthOff, mouthSize*2, mouthSize*3], pi, 0, 1)
        elif mouth == 'dot':
            mouthOff = int(self.size/5)
            mouthSize = int(mouthSize/2)
            pygame.gfxdraw.filled_circle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
            pygame.gfxdraw.aacircle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
        else:
            pygame.draw.aaline(self.screen, BLACK,(self.x-mouthSize,self.y+mouthOff),(self.x+mouthSize,self.y+mouthOff))

if __name__ == "__main__":
    FaceSize  = 100
    pygame.init()
    screen = pygame.display.set_mode([FaceSize, FaceSize])
    face = squareFace(FaceSize/2,FaceSize/2,FaceSize)
    face.draw(screen)
    pygame.display.update()         # update the screen with what we've drawn.
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()

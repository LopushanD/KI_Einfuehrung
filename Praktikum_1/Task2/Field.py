import pygame
from Grid import *


        


        
        
    
class Field:
    def __init__(self,size:tuple[int,int],verticalStep,horizontalStep,background=(0,0,0),foreground=(255,255,255),fontSize=14):
        pygame.init()
        
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fontSize = fontSize
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize) # text font
        self.background = background
        self.foreground = foreground
        
        self.stepV = verticalStep
        self.stepH = horizontalStep
        
        #self.gridSize = (self.size[0]-self.stepH,self.size[1]-self.stepV)
        
        self.done = False
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        
    def addGrid(self,grid:Grid):
        self.grid = grid
        self.stepV = self.grid.rectHeight+self.grid.margin
        self.stepH = self.grid.rectWidth+self.grid.margin
    
    def run(self):
        self.screen.fill(self.background)
        self.drawNumbers()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
            
            
            self.drawGrid()
            #self.drawObstacles(self.grid.obstacles)
            pygame.display.flip()

            self.clock.tick(60)
        pygame.quit()
    
    def drawGrid(self):
        for i in range(self.stepH,self.grid.size[0],self.stepH):
            xPos = (i - self.stepH) // self.stepH
            for j in range(0,self.grid.size[1]-self.stepV,self.stepV):
                yPos = j// self.stepV
                if self.grid.grid[xPos][yPos].nodeType == self.grid.NODE_VISITED:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.NODE_OBSTACLE):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.NODE_GOAL):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.NODE_START):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_START,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))

                else:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_UNVISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
        
                    
                
    
    def drawNumbers(self):
        counter = (self.grid.size[0]-self.stepV)//self.stepV+1
        coordinatesV = (((self.stepH)//4,(self.stepH)//2),self.stepV//4)
        #draw vertical lines
        for i in range(0,self.grid.size[1]-self.stepV,self.stepV):
            textV = self.font.render(str(counter), True, self.foreground,self.background)
            if(counter>9):
                self.screen.blit(textV,(coordinatesV[0][0],i+coordinatesV[1]))
            else:
                self.screen.blit(textV,(coordinatesV[0][1],i+coordinatesV[1]))
            counter-=1
        counter=1
        coordinateH =(self.grid.rectWidth//self.fontSize*3,self.grid.rectWidth//self.fontSize)
        #draw horizontal lines
        for i in range(self.stepH,self.grid.size[1],self.stepH):
                
            textH = self.font.render(str(counter), True,self.foreground, self.background)
            # make steps between numbers look more equal
            if(i>10):
                # self.screen.blit(textH,(i+self.grid.rectWidth//8,self.gridSize[1]-RECT_WIDTH))
                self.screen.blit(textH,(i+coordinateH[0],self.grid.size[1]-self.grid.rectHeight//2))
            else:
                self.screen.blit(textH,(i+coordinateH[1],self.grid.size[1]-self.grid.rectHeight//2))
            counter+=1


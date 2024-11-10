import pygame
from Grid import *
from AStar import *

        
# field is where our drawing takes place
class Field():
    def __init__(self,size:tuple[int,int],background=(0,0,0),foreground=(255,255,255)):
        # super().__init__()
        # self.terminate = threading.Event()
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.background = background
        self.foreground = foreground
        
        self.stepV = None
        self.stepH = None

        self.fontSize = None
        self.font = None # text font
        
        self.done = False
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        
    def addGrid(self,grid:Grid):
        self.grid = grid
        self.stepV = self.grid.rectHeight+self.grid.margin
        self.stepH = self.grid.rectWidth+self.grid.margin
        self.fontSize = round(self.grid.rectWidth*1)
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
    
    # def run(self):
    #     self.begin()
    
    def begin(self):
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
        # self.terminate.set()
        pygame.quit()
        
    
    def drawGrid(self):
        #we begin not from 0, but from 1.5 Cube width, because we need space for vertical numbers(row numbers). 0.5 Cube width is padding between number and cubes
        for i in range(round(self.stepH*1.5),self.grid.size[0],self.stepH):
            xPos = (i - self.stepH) // self.stepH
            for j in range(0,self.grid.size[1]-self.stepV,self.stepV):
                yPos = j// self.stepV
                #print("Node type {self.grid.grid[xPos][yPos].nodeType} will be painted")
                if(self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_START):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_START,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_VISITED:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_OBSTACLE):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_GOAL):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_BEST_WAY):           
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_BEST_WAY,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                else:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_UNVISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
        
                    
                
    
    def drawNumbers(self):
        #counter is a number drawn. For vertical numbers it goes from maximum to zero, for horizontal from zero to maximum
        counter = (self.grid.size[0]-self.stepV)//self.stepV+1
        
        verticalOffsetFromCubeLeftBottom = self.fontSize//2
        maxRowNumber = counter
        while(maxRowNumber//10 >0):
            self.fontSize = round(self.fontSize*0.75)
            verticalOffsetFromCubeLeftBottom = self.fontSize//2
            maxRowNumber = maxRowNumber//10
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        #draw vertical lines
        for i in range(0,self.grid.size[1]-self.stepV,self.stepV):
            textV = self.font.render(str(counter), True, self.foreground,self.background)
            
            self.screen.blit(textV,((self.stepH)//2,i+verticalOffsetFromCubeLeftBottom))
            counter-=1
        counter=1
        
        #setup correct font size for horizontal numbers, so that everything fits
        horizontalOffsetFromCubeLeftBottom = self.fontSize//2
        maxColumnNumber = (self.grid.size[1]-self.stepH)//self.stepH+1
        while(maxColumnNumber//10 >0):
            self.fontSize = round(self.fontSize*0.75)
            horizontalOffsetFromCubeLeftBottom = self.fontSize//2
            maxColumnNumber = maxColumnNumber//10
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        # draw horizontal numbers
        for i in range(round(self.stepH*1.5),self.grid.size[1],self.stepH):
            textH = self.font.render(str(counter), True,self.foreground, self.background)                        
            self.screen.blit(textH,(i+horizontalOffsetFromCubeLeftBottom,self.grid.size[1]+self.grid.rectHeight//2))
            counter+=1


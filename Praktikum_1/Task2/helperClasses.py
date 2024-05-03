import pygame
import math

# Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# RECT_WIDTH = 20
# RECT_HEIGHT = 20
# MARGIN = 2

class Grid:
    def __init__(self,size=(500,500),rectWidth=20,rectHeight=20,margin=2,color=(255, 255, 255),background=(0, 0, 0),obstacles:list[tuple]=[]):
        self.obstacles = obstacles
        self.margin = margin
        self.rectHeight = rectHeight
        self.rectWidth = rectWidth
        self.color =color
        self.background = background
        #padding is equals to size of one rectangle
        self.size = (size[0]-self.rectHeight,size[1]-self.rectWidth)
        
    def addObstacles(self,obstacles:list[tuple]):
        for obstacle in obstacles:
            self.obstacles.append(obstacle)
        
        
    
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
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
            self.screen.fill(self.background)
            
            
            self.drawNumbers()
            self.drawGrid()
            self.drawObstacles(self.grid.obstacles)
            pygame.display.flip()

            self.clock.tick(60)
        pygame.quit()
    
    def drawGrid(self):
        for i in range(2*self.stepV,self.grid.size[0],self.stepH):
            for j in range(0,self.grid.size[1]-2*self.stepV,self.stepV):
                
                pygame.draw.rect(self.screen,self.grid.color,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
    
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
            
    def drawObstacles(self,obstacles:list[tuple]):
        #obstacleBegan = False
        for i in range(self.stepH,self.grid.size[0],self.stepH):
            for j in range(0,self.grid.size[1]-self.stepV,self.stepV):
                
                pygame.draw.rect(self.screen,self.foreground,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
    
        for obstacle in obstacles:
            pygame.draw.rect(self.screen,self.background,pygame.Rect(obstacle[0],obstacle[1],abs(obstacle[0]-obstacle[2]),abs(obstacle[1]-obstacle[3])))
                    
import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

RECT_WIDTH = 20
RECT_HEIGHT = 20
MARGIN = 2

class Grid:
    def __init__(self,obstacles:list[tuple]=[]):
        self.obstacles = obstacles
        
        
    
class Field:
    def __init__(self,size:tuple[int,int]):
        pygame.init()
        
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.font = pygame.font.Font('freesansbold.ttf', 14) # text font
        
        self.stepV = MARGIN+RECT_HEIGHT
        self.stepH = MARGIN+RECT_WIDTH
        
        self.gridSize = (self.size[0]-self.stepH,self.size[1]-self.stepV)
        
        self.done = False
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
    
    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
            self.screen.fill(BLACK)
            self.drawGrid()
            self.drawNumbers()
            self.drawObstacles()
            pygame.display.flip()

            self.clock.tick(60)
        pygame.quit()
    
    def drawGrid(self):
        for i in range(2*self.stepV,self.gridSize[0],self.stepH):
            for j in range(0,self.gridSize[1]-2*self.stepV,self.stepV):
                
                pygame.draw.rect(self.screen,WHITE,pygame.Rect(i,j,RECT_WIDTH,RECT_HEIGHT))
    
    def drawNumbers(self):
        counter = (self.gridSize[0]-2*self.stepV)//self.stepV+1
        #draw vertical lines
        for i in range(0,self.gridSize[1]-2*self.stepV,self.stepV):
            textV = self.font.render(str(counter), True, WHITE,BLACK)
            self.screen.blit(textV,((RECT_WIDTH+MARGIN)//2,i+RECT_HEIGHT//4))
            counter-=1
        counter=1
        #draw horizontal lines
        for i in range(2*self.stepH,self.gridSize[1],self.stepH):
                
            textH = self.font.render(str(counter), True,WHITE, BLACK)
            # make steps between numbers look more equal
            if(i>10):
                self.screen.blit(textH,(i+RECT_WIDTH//8,self.gridSize[1]-RECT_WIDTH))
            else:
                self.screen.blit(textH,(i+RECT_WIDTH//4,self.gridSize[1]-RECT_WIDTH))
            counter+=1
            
    def drawObstacles(self):
        #obstacleBegan = False
        obstaclesFromTo = [(16*(RECT_WIDTH+MARGIN),0*(RECT_HEIGHT+MARGIN),17*(RECT_WIDTH+MARGIN),9*(RECT_HEIGHT+MARGIN)),(4*(RECT_WIDTH+MARGIN),9*(RECT_HEIGHT+MARGIN),
                        11*(RECT_WIDTH+MARGIN),10*(RECT_HEIGHT+MARGIN)),(10*(RECT_WIDTH+MARGIN),10*(RECT_HEIGHT+MARGIN),11*(RECT_WIDTH+MARGIN),0*(RECT_HEIGHT+MARGIN))]
        for i in range(2*self.stepH,self.gridSize[0],self.stepH):
            for j in range(0,self.gridSize[1]-2*self.stepV,self.stepV):
                
                pygame.draw.rect(self.screen,WHITE,pygame.Rect(i,j,RECT_WIDTH,RECT_HEIGHT))
    
        for obstacle in obstaclesFromTo:
            pygame.draw.rect(self.screen,BLACK,pygame.Rect(obstacle[0],obstacle[1],abs(obstacle[0]-obstacle[2]),abs(obstacle[1]-obstacle[3])))
                    
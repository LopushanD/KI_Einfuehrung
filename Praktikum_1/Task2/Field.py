import pygame
from Grid import *
from AStar import *
import utils
        
# field is where our drawing takes place
class Field():
    def __init__(self,size:tuple[int,int],paddingVertical = 20,paddingHorizontal=20,background=(0,0,0),foreground=(255,255,255)):
        # super().__init__()
        # self.terminate = threading.Event()
        pygame.init()
        self.paddingV = paddingVertical
        self.paddingH = paddingHorizontal
        
        self.sizeH = size[0]+self.paddingH+self.paddingH
        self.sizeV = size[1]+self.paddingV+self.paddingV
        self.screen = pygame.display.set_mode((self.sizeH,self.sizeV))
        self.background = background
        self.foreground = foreground
        
        self.stepV = None
        self.stepH = None

        self.fontSize = None
        self.font = None # text font
        
        self.done = False
        self.readyToStartAlgorithm = False
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        
    def addGrid(self,grid:Grid):
        self.grid = grid
        self.stepV = self.grid.rectHeight+self.grid.margin
        self.stepH = self.grid.rectWidth+self.grid.margin
        self.fontSize = round(self.grid.rectWidth*1)
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
    
    def begin(self):
        self.screen.fill(self.background)
        self.drawNumbers()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEMOTION:
                        left,middle,right = pygame.mouse.get_pressed()
                        x,y = pygame.mouse.get_pos()
                        #its just for debugging purposes, remove it later
                        if(event.type == pygame.KEYDOWN):
                            print(f"cursor position(x,y): {x}, {y}")
                            print(f"field size in pixels(x,y): {self.sizeH}, {self.sizeV}")
                            print(f"grid size in pixels(x,y): {self.grid.sizeH}, {self.grid.sizeV}")
                            print(f"Indexes of the Tile(horizontal, vertical): {utils.getIndexesOfTile(x,y,self)}")
                            print(f"grid size in number of tiles(x,y): {len(self.grid.grid)}, {len(self.grid.grid)}")
                        # now tile index calculation is awkward, write function that will translate the position to tile index
                        if(utils.isPositionOnGrid(x,y,self)):
                            xPos,yPos = utils.getIndexesOfTile(x,y,self)
                            if(event.type == pygame.KEYDOWN):
                                print(f"Actual tile indexes that are written to:{xPos}, {yPos}")
                            if left and self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_UNVISITED:
                                self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_OBSTACLE
                            elif right and self.grid.grid[xPos][yPos].nodeType == self.grid.grid[xPos][yPos].NODE_OBSTACLE:
                                self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_UNVISITED
                            elif not self.readyToStartAlgorithm and middle:
                                self.readyToStartAlgorithm = True
                        
            self.drawGrid()
            #self.drawObstacles(self.grid.obstacles)
            pygame.display.flip()

            self.clock.tick(60)
        # self.terminate.set()
        pygame.quit()
    
    def drawGrid(self):
        #we begin not from 0, but from 1.5 Cube width, because we need space for vertical numbers(row numbers). 0.5 Cube width is padding between number and cubes
        for i in range(self.paddingH,self.grid.sizeH+self.paddingH,self.stepH):
            index_x = max(0,((i-self.paddingH)// self.stepH)) 
            for j in range(self.paddingV,self.grid.sizeV+self.paddingV,self.stepV):
                index_y = max(0,((j-self.paddingV)// self.stepV) )
                
                # print(f"Indexes are: {index_x}, {index_y} \n Size of grid: {len(self.grid.grid)}, {len(self.grid.grid)}")
                if(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_START):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_START,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_VISITED:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_OBSTACLE):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_GOAL):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_BEST_WAY):           
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_BEST_WAY,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                else:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_UNVISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
        
    def drawNumbers(self):
        #counter is a number drawn. For vertical numbers it goes from maximum to zero, for horizontal from zero to maximum
        counter = (self.grid.sizeV)//self.stepV
        
        verticalOffsetFromCubeLeftBottom = self.fontSize//2
        maxRowNumber = counter
        while(maxRowNumber//10 >0):
            self.fontSize = round(self.fontSize*0.75)
            verticalOffsetFromCubeLeftBottom = self.fontSize//2
            maxRowNumber = maxRowNumber//10
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        #draw vertical lines
        for i in range(self.paddingV,self.grid.sizeV+self.paddingV,self.stepV):
            textV = self.font.render(str(counter), True, self.foreground,self.background)
            
            self.screen.blit(textV,((self.stepH)//2,i+verticalOffsetFromCubeLeftBottom))
            counter-=1
        counter=1
        
        #setup correct font size for horizontal numbers, so that everything fits
        horizontalOffsetFromCubeLeftBottom = self.fontSize//2
        maxColumnNumber = (self.grid.sizeH)//self.stepH
        while(maxColumnNumber//10 >0):
            self.fontSize = round(self.fontSize*0.75)
            horizontalOffsetFromCubeLeftBottom = self.fontSize//2
            maxColumnNumber = maxColumnNumber//10
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        # draw horizontal numbers
        for i in range(self.paddingH,self.grid.sizeH+self.paddingH,self.stepH):
            textH = self.font.render(str(counter), True,self.foreground, self.background)                        
            self.screen.blit(textH,(i+horizontalOffsetFromCubeLeftBottom,self.grid.sizeV+self.paddingV+self.grid.rectHeight//2))
            counter+=1


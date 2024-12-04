import pygame
from Grid import *
from AStar import *
import utils
        
# field is where our drawing takes place
class Field():
    """this class handles all drawing on the screen.
    """
    def __init__(self,grid:Grid,paddingVertical = 30,paddingHorizontal=20,background=(0,0,0),foreground=(255,255,255)):
        pygame.init()
        
        self.paddingV = paddingVertical
        self.paddingH = paddingHorizontal
        
        self.grid = grid
        self.stepV = self.grid.rectHeight+self.grid.margin
        self.stepH = self.grid.rectWidth+self.grid.margin
        
        self.sizeH = grid.sizeH+self.paddingH+self.paddingH+grid.rectWidth
        self.sizeV = grid.sizeV+self.paddingV+self.paddingV+grid.rectHeight
        
        self.fontSize = self.grid.rectWidth
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        self.screen = pygame.display.set_mode((self.sizeH,self.sizeV))
        self.background = background
        self.foreground = foreground
        
        self.endProgram = False
        self.readyToStartAlgorithm = False
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
    
    def begin(self):
        """starts drawing on screen
        """
        self.screen.fill(self.background)
        self.drawNumbers()
        startSet: bool = False
        goalSet: bool = False
        while not self.endProgram:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.endProgram = True
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEMOTION:
                        left,middle,right = pygame.mouse.get_pressed()
                        xPos,yPos = pygame.mouse.get_pos()
                        if(event.type == pygame.KEYDOWN):
                            print(f"{xPos} {yPos}")
                        if(utils.isPositionOnGrid(xPos,yPos,self)):
                            xIndex,yIndex = utils.getIndexesOfTile(xPos,yPos,self)
                            #draw obstacle
                            if left and self.grid.grid[xIndex][yIndex].nodeType ==self.grid.grid[xIndex][yIndex].NODE_UNVISITED:
                                self.grid.grid[xIndex][yIndex].nodeType = self.grid.grid[xIndex][yIndex].NODE_OBSTACLE
                            #clear obstacle
                            elif right and self.grid.grid[xIndex][yIndex].nodeType == self.grid.grid[xIndex][yIndex].NODE_OBSTACLE:
                                self.grid.grid[xIndex][yIndex].nodeType = self.grid.grid[xIndex][yIndex].NODE_UNVISITED
                            #reset everything if algorithm is running
                            elif self.readyToStartAlgorithm:
                                if middle:
                                    self.readyToStartAlgorithm = startSet = goalSet = False
                                    self.grid.populateGridWithClearNodes()
                            #prepare start, goal and obstacles before starting algorithm
                            else:
                                if middle and startSet and goalSet:
                                    self.readyToStartAlgorithm = True
                                else:
                                    startSet,goalSet = self._prepareNodesOnGrid(left,right,event.type,xIndex,yIndex,startSet,goalSet)                         
                                    
            self.updateGrid()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        

    
    def updateGrid(self):
        start = time.time()
        for i in range(self.paddingH,self.grid.sizeH+self.paddingH,self.stepH):
            index_x = utils.getXIndexOfTile(i,self)
            for j in range(self.paddingV,self.grid.sizeV+self.paddingV,self.stepV):
                index_y = utils.getYIndexOfTile(j,self)
                
                # print(f"Indexes: {index_x}, {index_y} \n Size of grid: {len(self.grid.grid[0])}, {len(self.grid.grid)}")
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
        end = time.time()
        print(f"Time to draw 1 frame: {(end-start)} sec")
        
    def drawNumbers(self):
        """draws numbers on x and y axes
        """
        #counter is a number drawn. For vertical numbers it goes from maximum to zero, for horizontal from zero to maximum
        counter = (self.grid.sizeV)//self.stepV
        
        verticalOffsetFromCubeLeftBottom = 0 #self.fontSize//4
        maxRowNumber = counter
        while(maxRowNumber//10 >0):
            self.paddingH+=self.fontSize
            maxRowNumber = maxRowNumber//10
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        #draw vertical lines
        for i in range(self.paddingV,self.grid.sizeV+self.paddingV,self.stepV):
            textV = self.font.render(str(counter), True, self.foreground,self.background)
            
            self.screen.blit(textV,((self.stepH)//2,i+verticalOffsetFromCubeLeftBottom))
            counter-=1
        counter=1
        
        #setup correct font size for horizontal numbers, so that everything fits
        maxColNumber = (self.grid.sizeH)//self.stepH
        while self.font.size(str(maxColNumber))[0] > self.grid.rectWidth:
                self.fontSize = self.fontSize-1
                self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        horizontalOffsetFromCubeLeftBottom = 0
        # draw horizontal numbers
        for i in range(self.paddingH,self.grid.sizeH+self.paddingH,self.stepH):
            textH = self.font.render(str(counter), True,self.foreground, self.background)                        
            self.screen.blit(textH,(i+horizontalOffsetFromCubeLeftBottom,self.grid.sizeV+self.paddingV+self.grid.rectHeight//2))
            counter+=1

    def _prepareNodesOnGrid(self,left,right,eventType,xPos,yPos,startSet,goalSet)-> tuple[bool,bool]:
        # there's png file, where code is depicted as state machine
        if left and eventType == pygame.MOUSEBUTTONDOWN:
            if self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_OBSTACLE:
                if not startSet:
                    self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_START
                    self.grid.start = (xPos,yPos)
                    startSet = True
                elif not goalSet:
                    self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_GOAL
                    self.grid.goal = (xPos,yPos)
                    goalSet = True
                else:
                    #do nothing
                    pass    
            elif self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_START:
                startSet = False
                if not goalSet:
                    self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_GOAL
                    self.grid.goal = (xPos,yPos)
                    goalSet = True
                else:
                    self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_UNVISITED
                    
            elif self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_GOAL:
                goalSet = False
                self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_UNVISITED
        elif right:
            if self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_START:
                startSet = False
            elif self.grid.grid[xPos][yPos].nodeType ==self.grid.grid[xPos][yPos].NODE_GOAL:
                goalSet = False
            self.grid.grid[xPos][yPos].nodeType = self.grid.grid[xPos][yPos].NODE_UNVISITED
        return (startSet,goalSet)
import pygame
from Grid import *
from AStar import *
from DrawingInformationHolder import *
import utils
        
# field is where our drawing takes place
class Field():
    """this class handles all drawing on the screen.
    """
    def __init__(self,grid:Grid,paddingVertical = 30,paddingHorizontal=20,background=(0,0,0),foreground=(255,255,255)):
        self.pygame = pygame
        self.pygame.init()
        
        self.paddingV = paddingVertical
        self.paddingH = paddingHorizontal
        
        self.grid = grid
        self.stepV = self.grid.rectHeight+self.grid.margin
        self.stepH = self.grid.rectWidth+self.grid.margin
        
        self.fontSize = self.grid.rectWidth
        self.font = self.pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        self.drawInformation = DrawingInformationHolder(self.grid,self.fontSize,paddingVertical,paddingHorizontal)
        
        self.sizeH = self.drawInformation.structure['fieldEndPosH']
        self.sizeV = self.drawInformation.structure['fieldEndPosV']
        
        self.screen = self.pygame.display.set_mode((self.sizeH,self.sizeV))
        self.background = background
        self.foreground = foreground
        
        self.endProgram = False
        self.readyToStartAlgorithm = False
        self.pygame.display.set_caption("My Game")
        self.clock = self.pygame.time.Clock()
    
    def begin(self):
        """starts drawing on screen
        """
        self.screen.fill(self.background)
        self.drawNodeLegend()
        self.drawNumbers()
        startSet: bool = False
        goalSet: bool = False
        while not self.endProgram:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                        self.endProgram = True
                else:
                    if event.type == self.pygame.MOUSEBUTTONDOWN or self.pygame.MOUSEMOTION:
                        left,middle,right = self.pygame.mouse.get_pressed()
                        xPos,yPos = self.pygame.mouse.get_pos()
                        # if(event.type == self.pygame.KEYDOWN):
                        #     print(f"{xPos} {yPos}")
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
            self.pygame.display.flip()
            self.clock.tick(60)
        self.pygame.quit()
        

    
    def updateGrid(self):
        # start = time.time()
        for i in range(self.drawInformation.gridTiles["beginPosH"],self.drawInformation.gridTiles["endPosH"],self.stepH):
            index_x = utils.getXIndexOfTile(i,self)
            for j in range(self.drawInformation.gridTiles["beginPosV"],self.drawInformation.gridTiles["endPosV"],self.stepV):
                index_y = utils.getYIndexOfTile(j,self)
                
                # print(f"Indexes: {index_x}, {index_y} \n Size of grid: {len(self.grid.grid[0])}, {len(self.grid.grid)}")
                if(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_START):
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_START,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_VISITED:
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_OBSTACLE):
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_GOAL):
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[index_x][index_y].nodeType == self.grid.grid[index_x][index_y].NODE_BEST_WAY):           
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_BEST_WAY,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                else:
                    self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_UNVISITED,self.pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
        # end = time.time()
        # print(f"Time to draw 1 frame: {(end-start)} sec")
        
    def drawNumbers(self):
        """draws numbers on x and y axes
        """
        #counter is a number drawn. For vertical numbers it goes from maximum to zero, for horizontal from zero to maximum
        counter = (self.grid.sizeV)//self.stepV
        
        #draw vertical lines
        for i in range(self.drawInformation.numbersV['beginPosV'],self.drawInformation.numbersV['endPosV'],self.stepV):
            textV = self.font.render(str(counter), True, self.foreground,self.background)
            
            self.screen.blit(textV,(self.drawInformation.numbersV['beginPosH'],i))
            counter-=1
        counter=1
        
        #setup correct font size for horizontal numbers, so that everything fits
        maxColNumber = (self.grid.sizeH)//self.stepH
        fontTmp = self.fontSize
        while self.font.size(str(maxColNumber))[0] > self.grid.rectWidth:
            fontTmp = fontTmp-1
            self.font = self.pygame.font.Font('freesansbold.ttf', fontTmp)
        # draw horizontal numbers
        for i in range(self.drawInformation.numbersH['beginPosH'],self.drawInformation.numbersH['endPosH'],self.stepH):
            textH = self.font.render(str(counter), True,self.foreground, self.background)                        
            self.screen.blit(textH,(i,self.drawInformation.numbersH['beginPosV']))
        
            counter+=1
        self.font = self.pygame.font.Font('freesansbold.ttf', self.fontSize)


    def drawNodeLegend(self):
        horizontalOffsetFromCubeLeftBottom = 0
        
        drawPosV = self.drawInformation.legendTile['beginPosV']
        drawPosH = self.drawInformation.legendTile['beginPosH']
        
        legendRectWidth = self.grid.rectWidth*4
        addToOffset = legendRectWidth+self.grid.rectWidth
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_START,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_BEST_WAY,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.pygame.draw.rect(self.screen,self.grid.COLOR_NODE_UNVISITED,self.pygame.Rect(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,self.grid.rectHeight))
        horizontalOffsetFromCubeLeftBottom+= addToOffset
        
        drawPosV = self.drawInformation.legendTileLabel['beginPosV']
        textFieldHeight = self.drawInformation.legendTileLabel['beginPosV'] - self.drawInformation.legendTileLabel['endPosV']
        horizontalOffsetFromCubeLeftBottom = 0
        fontTmp = 12
        self.font = self.pygame.font.Font('freesansbold.ttf', fontTmp)
        texts = ["start node","visited node","obstacle node","goal node", "best way node", "unvisited node"]
        for text in texts:                        
            tmp = self.font.render(text, True,self.foreground, self.background)
            self.screen.blit(tmp,(drawPosH+horizontalOffsetFromCubeLeftBottom,drawPosV,legendRectWidth,textFieldHeight))
            horizontalOffsetFromCubeLeftBottom+= addToOffset
        self.font = self.pygame.font.Font('freesansbold.ttf', self.fontSize)
        
            

    def _prepareNodesOnGrid(self,left,right,eventType,xPos,yPos,startSet,goalSet)-> tuple[bool,bool]:
        # there's png file, where code is depicted as state machine
        if left and eventType == self.pygame.MOUSEBUTTONDOWN:
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
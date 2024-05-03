import pygame
import math


class Grid:
    def __init__(self,start:tuple,goal:tuple,size=(500,500),rectWidth=20,rectHeight=20,margin=2):
        self.margin = margin
        self.rectHeight = rectHeight
        self.rectWidth = rectWidth
        
        self.COLOR_NODE_VISITED =(0, 0, 255) #blue
        self.COLOR_NODE_GOAL = (0, 255, 0) #green
        self.COLOR_NODE_OBSTACLE = (255,0,0) #red
        self.COLOR_NODE_UNVISITED = (255,255,255) #white
        self.COLOR_NODE_START = (255,255,0)#yellow 
        self.COLOR_NODE_BEST_WAY = (0,0,0)# black
        self.COLOR_BACKGROUND = (0,0,0)# black
        #padding is equals to size of one rectangle
        self.size = (size[0]-self.rectHeight,size[1]-self.rectWidth)
        
        #self.color =color
        #self.background = background
        
        #these numbers are based on the numbers that user sees near the grid 
        self.start = self.translateCoordinates(start[0],start[1])
        self.goal = self.translateCoordinates(goal[0],goal[1])
        #0 - unvisited tile, 1 - visited tile, 2 - obstacle tile
        self.grid = [[]]
        self.initGrid()
        
    def initGrid(self):
        sizeX = self.size[0]//(self.rectWidth+self.margin)
        sizeY = self.size[1]//(self.rectHeight+self.margin)
        self.grid = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
    
        self.grid[self.start[0]][self.start[1]] = 4
        self.grid[self.goal[0]][self.goal[1]] = 3
        
        
        
    #obstacle numbers are based on the numbers that user sees near the grid 
    def setObstacles(self,obstacles:list[tuple]):
        for obstacle in obstacles:
            xStart,yStart = self.translateCoordinates(obstacle[0],obstacle[3])
            xEnd,yEnd = self.translateCoordinates(obstacle[2],obstacle[1])
            #(obstacle[0]-1,(self.size[1]//(self.rectHeight+self.margin)-obstacle[3]),obstacle[2]-1,(self.size[1]//(self.rectHeight+self.margin))-obstacle[1])
            print(f" size: {self.size[1]//(self.rectHeight+self.rectWidth)} i: {xStart}->{xEnd} ; j: {yStart} -> {yEnd}")
            #(self.grid.size[0]-self.stepV)//self.stepV+1
            for i in range(xStart,xEnd):
                for j in range(yStart,yEnd):
                    #print(f"i: {i} ; j: {j}")
                    self.grid[i][j] = 2
    
    def translateCoordinates(self,x,y):
        return (x-1,self.size[1]//(self.rectHeight+self.margin)-y)
    
            
    
    
    def setVisited(self,x,y):
        self.grid[x][y]
        
        
        
    
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
            #self.drawObstacles(self.grid.obstacles)
            pygame.display.flip()

            self.clock.tick(60)
        pygame.quit()
    
    def drawGrid(self):
        for i in range(self.stepH,self.grid.size[0],self.stepH):
            xPos = (i - self.stepH) // self.stepH
            for j in range(0,self.grid.size[1]-self.stepV,self.stepV):
                yPos = j// self.stepV
                if self.grid.grid[xPos][yPos] == 1:
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_VISITED,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos] == 2):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_OBSTACLE,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos] == 3):
                    pygame.draw.rect(self.screen,self.grid.COLOR_NODE_GOAL,pygame.Rect(i,j,self.grid.rectWidth,self.grid.rectHeight))
                elif(self.grid.grid[xPos][yPos] == 4):
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
            
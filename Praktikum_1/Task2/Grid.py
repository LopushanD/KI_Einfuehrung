from Node import *
import time
class Grid:
    def __init__(self,start:tuple,goal:tuple,size=(500,500),rectWidth=20,rectHeight=20,margin=2,stepCost=1):
        self.margin = margin
        self.rectHeight = rectHeight
        self.rectWidth = rectWidth
        self.stepCost = stepCost
        
        self.COLOR_NODE_VISITED =(0, 0, 255) #blue
        self.COLOR_NODE_GOAL = (0, 255, 0) #green
        self.COLOR_NODE_OBSTACLE = (255,0,0) #red
        self.COLOR_NODE_UNVISITED = (255,255,255) #white
        self.COLOR_NODE_START = (255,255,0)#yellow 
        self.COLOR_NODE_BEST_WAY = (0,200,200)# cyan
        self.COLOR_BACKGROUND = (0,0,0)# black
        #padding is equals to size of one rectangle
        self.size = (size[0]-self.rectHeight,size[1]-self.rectWidth)
        
        
        #these numbers are based on the numbers that user sees near the grid 
        self.start = self.translateCoordinates(start[0],start[1])
        self.goal = self.translateCoordinates(goal[0],goal[1])
        #0 - unvisited tile, 1 - visited tile, 2 - obstacle tile
        self.grid = [[]]
        # self.initNodes()
        self.initGrid()
        
    def initGrid(self):
        self.initNodes()
        
        self.grid[self.start[0]][self.start[1]].nodeType = self.grid[self.start[0]][self.start[1]].NODE_START 
        self.grid[self.start[0]][self.start[1]].posDim1 = self.start[0]
        self.grid[self.start[0]][self.start[1]].posDim2 = self.start[1]
        
        
        self.grid[self.goal[0]][self.goal[1]].nodeType = self.grid[self.goal[0]][self.goal[1]].NODE_GOAL
        self.grid[self.goal[0]][self.goal[1]].posDim1 = self.goal[0]
        self.grid[self.goal[0]][self.goal[1]].posDim2 = self.goal[1]
        
    def initNodes(self):
        sizeX = self.size[0]//(self.rectWidth+self.margin)
        sizeY = self.size[1]//(self.rectHeight+self.margin)
        #creates new Node instance in each grid tile
        self.grid = [[Node(i,j) for j in range(sizeY)] for i in range(sizeX)]
        
        #add neigboors to corner Tiles
        
        #top left
        self.grid[0][0].addNeighboor(self.grid[0][1])
        self.grid[0][0].addNeighboor(self.grid[1][0])
        #top right
        self.grid[0][sizeY-1].addNeighboor(self.grid[0][sizeY-2])
        self.grid[0][sizeY-1].addNeighboor(self.grid[1][sizeY-1])
        #bottom left
        self.grid[sizeX-1][0].addNeighboor(self.grid[sizeX-2][0])
        self.grid[sizeX-1][0].addNeighboor(self.grid[sizeX-1][1])
        #bottom right
        self.grid[sizeX-1][sizeY-1].addNeighboor(self.grid[sizeX-2][sizeY-1])
        self.grid[sizeX-1][sizeY-1].addNeighboor(self.grid[sizeX-1][sizeY-2])
        
       #add neighboors to inner tiles
        for i in range(1,sizeX-1):
            for j in range(1,sizeY-1):
                self.grid[i][j].addNeighboor(self.grid[i][j-1])
                self.grid[i][j].addNeighboor(self.grid[i][j+1])
                self.grid[i][j].addNeighboor(self.grid[i-1][j])
                self.grid[i][j].addNeighboor(self.grid[i+1][j])
                
        #add neighboors to Outter tiles (except corner tiles)
         
        #add neighboors to outter left tile 
        for i in range(1,sizeX-1):
            self.grid[i][0].addNeighboor(self.grid[i-1][0])
            self.grid[i][0].addNeighboor(self.grid[i+1][0])
            self.grid[i][0].addNeighboor(self.grid[i][1])        
            
            #add neighboors to outter right tile           
            self.grid[i][sizeY-1].addNeighboor(self.grid[i-1][sizeY-1])
            self.grid[i][sizeY-1].addNeighboor(self.grid[i+1][sizeY-1])
            self.grid[i][sizeY-1].addNeighboor(self.grid[i][sizeY-2])
        
        for j in range(1,sizeY-1):
            #add neighboors to outter top tile
            self.grid[0][j].addNeighboor(self.grid[0][j-1])
            self.grid[0][j].addNeighboor(self.grid[0][j+1])
            self.grid[0][j].addNeighboor(self.grid[1][j])        
            
            #add neighboors to outter bottom tile           
            self.grid[sizeX-1][j].addNeighboor(self.grid[sizeX-1][j-1])
            self.grid[sizeX-1][j].addNeighboor(self.grid[sizeX-1][j+1])
            self.grid[sizeX-1][j].addNeighboor(self.grid[sizeX-2][j])
              
        
    #obstacle numbers are based on the numbers that user sees near the grid 
    def setObstacles(self,obstacles:list[tuple]):
        for obstacle in obstacles:
            xStart,yStart = self.translateCoordinates(obstacle[0],obstacle[3])
            xEnd,yEnd = self.translateCoordinates(obstacle[2],obstacle[1])
            
            for i in range(xStart,xEnd):
                for j in range(yStart+1,yEnd+1):
                    #print(f"i: {i} ; j: {j}")
                    self.grid[i][j].nodeType = self.grid[i][j].NODE_OBSTACLE
                    self.grid[i][j].posDim1 = i
                    self.grid[i][j].posDim2 = j
                    
    def clearObstacles(self,obstacles:list[tuple]):
        """TO BE IMPLEMENTED !!!"""
        pass
                    
    def translateCoordinates(self,x,y):
        """ translates coordinates from from user's point of view (0,0 is bottom left) to PyGame's point of view (0,0 is top left)
        coordinate entity is 1 tile, not 1 pixel. For example if tile is 10x10 pixels, then coordinate(3,3) is at (30,30) pixels   

        Args:
            x,y: coordinates from user's point of view (0,0 is bottom left)
            
        Returns coordinates from PyGame's point of view (0,0 is top left)
        """
        return (x-1,self.size[1]//(self.rectHeight+self.margin)-y)
    
    #go from end to begin marking best steps
    def markAsBestWay(self,node:Node):
        node.nodeType = node.NODE_GOAL
        #take the best parent of end node
        nextNode = sorted(node.getParents(),key=lambda x:x.cost,reverse=False)[0]
        #special cases: start == end,step -> end, start->intermediate step -> end
        if(node.parents[0] == node.parents[0].parents[0]):
            return
        elif(node.parents[0].parents[0] == node.parents[0].parents[0].parents[0]):
            node.parents[0].nodeType = node.NODE_BEST_WAY
            return
        
        while True:
            #just for visualization purposes
            time.sleep(0.08)
            if(nextNode == nextNode.parents[0]):
                break
            parentsToCheck = []
            for parent in nextNode.getParents():
                if(parent.nodeType != parent.NODE_BEST_WAY):
                    parentsToCheck.append(parent)
            #sort so that parent with smallest cost is at index 0
            parentsToCheck.sort(key=lambda x:x.cost,reverse=False)
            bestParent = parentsToCheck[0]
            nextNode.nodeType = nextNode.NODE_BEST_WAY
            nextNode = bestParent

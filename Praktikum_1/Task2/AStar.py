from Grid import *
import threading
import time
from utils import Queue
    
class AStar(threading.Thread):
    
    def __init__(self,grid:Grid,algorithmSpeed:int):
        self.SPEED_SLOW=1
        self.SPEED_FAST=2
        self.SPEED_INSTANT=3
        
        super().__init__()
        
        self.algorithmSpeed = None
        self.setAlgorithmSpeed(algorithmSpeed)
        
        self.grid = grid
        self.startNode:Node = None #grid.grid[grid.start[0]][grid.start[1]]
        self.endNode =  None #grid.grid[grid.goal[0]][grid.goal[1]]
        
        self.terminate = threading.Event()
        
        self.open = Queue()
        self.stepCost = grid.stepCost
        
        
    def interruptThread(self):
        self.terminate.set()
    
    def setStartAndEndPoint(self):
        self.endNode = self.grid.grid[self.grid.goal[0]][self.grid.goal[1]]
        
        self.startNode:Node = self.grid.grid[self.grid.start[0]][self.grid.start[1]]
        self.startNode.setCost(0)
        self.startNode.addParent(self.startNode)
        
        self.open.enque(self.startNode)
        
    def setAlgorithmSpeed(self,speed)->None:
        if(speed ==self.SPEED_SLOW):
            self.algorithmSpeed = 0.05
        elif(speed ==self.SPEED_FAST):
            self.algorithmSpeed = 0.01
        elif(speed==self.SPEED_INSTANT):
            self.algorithmSpeed = 0
        else:
            raise(RuntimeError.add_note("Wrong algorithm speed was given as a parameter"))
        
    def run(self):
        self.setStartAndEndPoint()
        self.search()
        # self.startNode.setNodeType(self.startNode.NODE_START)
        self.grid.markAsBestWay(self.endNode)
        # self.startNode.setNodeType(self.startNode.NODE_START)
        self.interruptThread()
        
    def search(self)-> None:
        
        while self.open.qNotEmpty() and not self.terminate.is_set():
            # print(f"Is set: {self.terminate.is_set()}")
            #just for visualization purposes
            time.sleep(self.algorithmSpeed)

            currentNode = self.open.deque()
            #don't need to check ways that are obviously worse
            if(currentNode.cost >= self.endNode.cost):
                continue
            
            for neighboor in currentNode.getNeighboors():
                
                if(neighboor.isNotVisited() and neighboor.isNotObstacle()):
                    # step cost from one tile to another is defined in grid, by default it's 1. here we have Theoretical + actual distances 
                    newCost = currentNode.cost+self.stepCost+currentNode.findTheoreticalDistanceToGoal(self.endNode)
                    # update node path cost if it's improved
                    if(newCost < neighboor.cost + neighboor.findTheoreticalDistanceToGoal(self.endNode)):
                        neighboor.setCost(newCost)
                        neighboor.addParent(currentNode)
                        neighboor.setVisited()
                        self.open.enque(neighboor)
            
            
                        
                        
                        
            
                
        
        
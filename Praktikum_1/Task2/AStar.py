from Grid import *
import threading
import time
import heapq
class Queue:
    def __init__(self):
        
        self.q = []
    
    def enque(self,element:"Node"):
        heapq.heappush(self.q,(element))
    
    
    def qNotEmpty(self)-> bool:
        if(len(self.q)>0):
            return True
        return False
            
    def deque(self) -> "Node":
        return heapq.heappop(self.q)
    
    def isInQueue(self,element:object) -> bool:
        if element in self.q:
            return True
        return False
    
    
class AStar(threading.Thread):
    def __init__(self,grid:Grid):
        super().__init__()
        self.grid = grid
        self.terminate = threading.Event()
        self.startNode:Node = grid.grid[grid.start[0]][grid.start[1]]
        self.endNode = grid.grid[grid.goal[0]][grid.goal[1]]
        self.open = Queue()
        self.stepCost = grid.stepCost
        
        self.startNode.setCost(0)
        self.startNode.addParent(self.startNode)
        self.open.enque(self.startNode)
        
    def interruptThread(self):
        self.terminate.set()
        
    def run(self):
        self.search()
        # self.startNode.setNodeType(self.startNode.NODE_START)
        self.grid.markAsBestWay(self.endNode)
        # self.startNode.setNodeType(self.startNode.NODE_START)
        self.interruptThread()
        
    def search(self)-> None:
        
        while self.open.qNotEmpty():
            #just for visualization purposes
            time.sleep(0.02)

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
            
            
                        
                        
                        
            
                
        
        
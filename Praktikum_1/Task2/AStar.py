from Grid import *
import threading
import time
class Queue:
    def __init__(self):
        
        self.q = []
    
    #it's vice versa (worst -> best ). it's to reduce time complexity
    def bestEnque(self,element:object):
        self.q.insert(0,element)
    
    def notBestEnque(self,element:object):
        self.q.insert(-1,element)
    
    def qNotEmpty(self)-> bool:
        if(len(self.q)>0):
            return True
        return False
            
    def bestDeque(self) -> object:
        return self.q.pop(0)
    
    def isInQueue(self,element:object) -> bool:
        if element in self.q:
            return True
        return False
    
    
    #better not to use, cause of O(n) time
    def worstDeque(self) -> object:
        return self.q.pop(0)
    
class AStar(threading.Thread):
    def __init__(self,grid:Grid):
        super().__init__()
        self.grid = grid
        self.terminate = threading.Event()
        self.startNode:Node = grid.grid[grid.start[0]][grid.start[1]]
        self.endNode = grid.grid[grid.goal[0]][grid.goal[1]]
        self.open = Queue()
        #self.closed = Queue()
        self.startNode.setCost(0)
        self.startNode.addParent(self.startNode)
        self.open.bestEnque(self.startNode)
        
    def interruptThread(self):
        self.terminate.set()
        
    def run(self):
        self.search()
        self.grid.markAsBestWay(self.endNode)
        self.startNode.setNodeType(self.startNode.NODE_START)
        self.interruptThread()
        
    def search(self)-> None:
        
        while self.open.qNotEmpty():
            time.sleep(0.1)
            currentNode:Node = self.open.worstDeque()
            # if(not currentNode.isNotVisited()):
            #     continue
            if(currentNode == self.endNode):
                break
            for neighboor in currentNode.getNeighboors():
                
                if(neighboor.isNotVisited() and neighboor.isNotObstacle()):
                # if(neighboor.isNotObstacle()):
                    if(currentNode.cost + 1 +currentNode.findTheoreticalDistanceToGoal(self.endNode) < neighboor.cost + neighboor.findTheoreticalDistanceToGoal(self.endNode)):
                        neighboor.setCost(currentNode.cost+1+currentNode.findTheoreticalDistanceToGoal(self.endNode))
                        neighboor.addParent(currentNode)
                        self.open.bestEnque(neighboor)
            currentNode.setVisited()                               
                
            # currentNode.setVisited()
            
                        
                        
                        
            
                
        
        
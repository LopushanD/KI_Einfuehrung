from Grid import *
import threading
import time
import heapq
class Queue:
    def __init__(self):
        
        self.q = []
    
    #it's vice versa (worst -> best ). it's to reduce time complexity
    def enque(self,element:"Node"):
        heapq.heappush(self.q,(element))
    
    # def notBestEnque(self,element:object):
    #     self.q.insert(-1,element)
    
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
    
    
    # #better not to use, cause of O(n) time
    # def worstDeque(self) -> object:
    #     return self.q.pop(0)
    
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
        self.open.enque(self.startNode)
        #heapq.heappush(self.open.q,(self.startNode.cost,self.startNode))
        
    def interruptThread(self):
        self.terminate.set()
        
    def run(self):
        self.search()
        self.grid.markAsBestWay(self.endNode)
        self.startNode.setNodeType(self.startNode.NODE_START)
        self.interruptThread()
        
    def search(self)-> None:
        
        while self.open.qNotEmpty():
            time.sleep(0.02)
            #currentCost, currentNode = heapq.heappop(self.open.q) # type: ignore
            currentNode = self.open.deque()
            if(currentNode.cost >= self.endNode.cost):
                continue
            # if(currentNode == self.endNode):
            #     break
            for neighboor in currentNode.getNeighboors():
                
                if(neighboor.isNotVisited() and neighboor.isNotObstacle()):
                # if(neighboor.isNotObstacle()):
                    newCost = currentNode.cost+1+currentNode.findTheoreticalDistanceToGoal(self.endNode)
                    if(newCost < neighboor.cost + neighboor.findTheoreticalDistanceToGoal(self.endNode)):
                        neighboor.setCost(newCost)
                        neighboor.addParent(currentNode)
                        neighboor.setVisited()
                        # heapq.heappush(self.open.q,(neighboor.cost,neighboor))
                        self.open.enque(neighboor)
            # currentNode.setVisited()                               
                
            # currentNode.setVisited()
            
                        
                        
                        
            
                
        
        
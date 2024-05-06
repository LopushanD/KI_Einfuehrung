from Grid import *
import threading
import time
class Queue:
    def __init__(self):
        
        self.q = []
    
    def enque(self,element:object) -> bool:
        self.q.insert(0,element)
        return True
    
    def qNotEmpty(self)-> bool:
        if(len(self.q)>0):
            return True
        return False
            
    def fifoDeque(self) -> object:
        return self.q.pop()
    
    
    
    def lifoDeque(self) -> object:
        return self.q.pop(0)
    
class AStar(threading.Thread):
    def __init__(self,grid:Grid):
        super().__init__()
        self.grid = grid
        self.terminate = threading.Event()
        self.startNode:Node = grid.grid[grid.start[0]][grid.start[1]]
        self.endNode = grid.grid[grid.goal[0]][grid.goal[1]]
        self.q = Queue()
        self.startNode.findTheoreticalDistanceToGoal(self.endNode)
        self.startNode.addParent(self.startNode)
        self.q.enque(self.startNode)
        
    def interruptThread(self):
        self.terminate.set()
        
    def run(self):
        self.search()
        self.grid.markAsBestWay(self.endNode)
        self.startNode.setNodeType(self.startNode.NODE_START)
        self.interruptThread()
        
    def search(self)-> None:
        #priorityVisit ={}
        while self.q.qNotEmpty():
            time.sleep(0.01)
            currentNode:Node = self.q.fifoDeque()
            if(not currentNode.isNotVisited()):
                continue
            if(currentNode == self.endNode):
                #self.grid.markAsBestWay(self.endNode.parent)
                break
            #print(f"x: {currentNode.posDim1}, y: {currentNode.posDim2}")
            nodesToGo = []
            for neighboor in currentNode.getNeighboors():
                #print(f"Neighboors of the node: -> x: {neighboor.posDim1}, y: {neighboor.posDim2}")
                if(neighboor.isNotVisited() and neighboor.isNotObstacle()):
                    neighboor.findTheoreticalDistanceToGoal(self.endNode)
                    #if(currentNode.valueToGoal>=neighboor.valueToGoal):
                    nodesToGo.append(neighboor)
                        #neighboor.parent = currentNode
                        #self.q.fifoEnque(neighboor)
            nodesToGo = sorted(nodesToGo,key=lambda x: x.valueToGoal,reverse=True)
            for node in nodesToGo:
                node.addParent(currentNode)
                self.q.enque(node)
                
            
            currentNode.setVisited()
            
                        
                        
                        
            
                
        
        
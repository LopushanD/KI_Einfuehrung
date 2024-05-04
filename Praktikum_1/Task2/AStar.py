from Grid import *
import threading
class Queue:
    def __init__(self):
        self.fifo = []
    
    def fifoEnque(self,element:object) -> bool:
        self.fifo.insert(0,element)
        return True
    
    def fifoNotEmpty(self)-> bool:
        if(len(self.fifo)>0):
            return True
        return False
            
    def fifoDeque(self) -> object:
        return self.fifo.pop()
class AStar(threading.Thread):
    def __init__(self,grid:Grid):
        super().__init__()
        self.terminate = threading.Event()
        self.startNode = grid.grid[grid.start[0]][grid.start[1]]
        self.endNode = grid.grid[grid.goal[0]][grid.goal[1]]
        self.q = Queue()
        self.startNode.parent = self.startNode
        self.q.fifoEnque(self.startNode)
        
    def interruptThread(self):
        self.terminate.set()
        
    def run(self):
        self.search()
        
    def search(self)-> None:
        #priorityVisit ={}
        while True:
            currentNode:Node = self.q.fifoDeque()
            
            if(currentNode == self.endNode):
                self.interruptThread()
            currentNode.setVisited()
            print(f"x: {currentNode.posDim1}, y: {currentNode.posDim2}")
            for neighboor in currentNode.getNeighboors():
                if(neighboor.isNotVisited()):
                    if(currentNode.findTheoreticalDistanceToGoal(self.endNode)>neighboor.findTheoreticalDistanceToGoal(self.endNode)):
                        neighboor.parent = currentNode
                        self.q.fifoEnque(neighboor)
            
                        
                        
                        
            
                
        
        
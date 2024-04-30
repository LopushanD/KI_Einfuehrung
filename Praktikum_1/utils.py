#from graph import Node
def getNode(name, l):
   return next(( i for i in l if i.name == name), -1)

class Tracker:
    """Tracks taken path and it's cost"""
    def __init__(self,startNode:object):
        self.path:str = startNode.name
        self.totalCost:int = 0    

    def update(self,nextNode:object,stepCost:int):
        self.path+=" -> "+nextNode.name
        self.totalCost+=stepCost
    def printPath(self):
        print(self.path)
        
    def printCost(self):
        print(self.totalCost)
    
    def printInfo(self):
        self.printPath()
        self.printCost()
        
class Queue:
    def __init__(self):
        self.fifo = []
        self.lifo = []
        self.prio = {}
    
    def fifoEnque(self,element:object) -> bool:
        self.fifo.insert(0,element)
        return True
    
    def fifoNotEmpty(self)-> bool:
        if(len(self.fifo)>0):
            return True
        return False
            
    def fifoDeque(self) -> object:
        return self.fifo.pop()
    
    def lifoEnque(self,element:object) -> bool:
        self.lifo.insert(0,element)
        return True
    
    def lifoNotEmpty(self)-> bool:
        if(len(self.lifo)>0):
            return True
        return False
    
    
    def lifoDeque(self) -> object:
        return self.lifo.pop(0)
    
def isNotCycle(parent,child,totalCostChild,exploredWays:list[tuple]) -> bool:
    for way in exploredWays:
        oneCity,otherCity,exploredPairCost = way
        if( ( (parent.name == oneCity.name and child.name == otherCity.name) or (parent.name == otherCity.name and child.name ==oneCity.name) ) and totalCostChild>=exploredPairCost ):
            return False
    return True
        
    # def prioEnque(self,priority:int,element:object) -> bool:
    #implement when it gets clear what to do with it      
    
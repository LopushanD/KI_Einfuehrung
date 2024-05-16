#from graph import Node
def getNode(name, l):
   return next(( i for i in l if i.name == name), -1)

     
class Queue:
    def __init__(self):
        self.fifo = []
        self.lifo = []
    
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

def printWay(node:object)->None:
    
    print("the way is: ",end='')
    while node.parent!=node:
        print(node.name+" <- ",end='')
        node = node.parent
    print(node.name)
        

def isNotCycle(parent,child,totalCostChild,exploredWays:list[tuple]) -> bool:
    # for the way to be a cycle, names of nodes must be on the list and total way cost must be bigger or equal than on the list 
    for way in exploredWays:
        oneCity,otherCity,exploredPairCost = way
        if( ( (parent.name == oneCity.name and child.name == otherCity.name) or (parent.name == otherCity.name and child.name ==oneCity.name) )
        and totalCostChild>=exploredPairCost ):
            return False
    return True
        
    
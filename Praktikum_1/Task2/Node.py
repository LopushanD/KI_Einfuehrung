import math
class Node:
    def __init__(self,pos1:int,pos2:int):
        
        self.NODE_UNVISITED=0
        self.NODE_VISITED=1
        self.NODE_OBSTACLE=2
        self.NODE_START=3
        self.NODE_GOAL=4
        self.NODE_BEST_WAY=5
        
        self.posDim1 = pos1
        self.posDim2 = pos2
        # basically means cost is infinity
        self.cost:float = 0xffffffff
        self.parents = []
        self.nodeType = self.NODE_UNVISITED
        self.neighboors = []
        
    def setVisited(self)->None:
        self.nodeType = self.NODE_VISITED
        
    def isNotVisited(self)->bool:
        if(self.nodeType == self.NODE_VISITED):
            return False
        return True
    
    def isNotObstacle(self)->bool:
        if(self.nodeType == self.NODE_OBSTACLE):
            return False
        return True
    
    def setNodeType(self,nodeType:int):
        self.nodeType = nodeType
        print(self.nodeType)
    
        
    def findTheoreticalDistanceToGoal(self,goal:object):
        # if(self.isNotObstacle()):
        return math.sqrt(math.pow(self.posDim1-goal.posDim1,2) + math.pow(self.posDim2 - goal.posDim2,2))
    
    def setCost(self,number:float):
        self.cost = number
    
    #override of check "lower than" in priority queue, so that it works with Node class
    def __lt__(self,other: "Node"):
        return self.cost < other.cost
    
    def addNeighboor(self,node:object):
        self.neighboors.append(node)
    
    def getNeighboors(self) -> list[object]: # type: ignore
        return self.neighboors
    
    def getParents(self):
        return self.parents
    
    def addParent(self,parent:object):
        self.parents.append(parent)
    
    
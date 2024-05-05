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
        self.valueToGoal:float = 0xffffffff
        self.parents = []
        self.nodeType = 0
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
    
        
    def findTheoreticalDistanceToGoal(self,goal:object):
        # if(self.isNotObstacle()):
        self.valueToGoal = math.sqrt(math.pow(self.posDim1-goal.posDim1,2) + math.pow(self.posDim2 - goal.posDim2,2))
        # return 0xfffffffe # so that if we add 1 (cost of step), it doesn't flip to 0
        
    # def addNeighboors(self,nodesAndNeighboors:tuple[list[object],list[list[object]]]):
    #     for node,neighboors in nodesAndNeighboors:
    #         self.addNeighboor(node)
    
    def addNeighboor(self,node:object):
        self.neighboors.append(node)
    
    def getNeighboors(self) -> list[object]: # type: ignore
        return self.neighboors
    
    def getParents(self):
        return self.parents
    
    def addParent(self,parent:object):
        self.parents.append(parent)
    
    
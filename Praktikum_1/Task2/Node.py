import math
class Node:
    def __init__(self,pos1:int,pos2:int):
        
        
        self.posDim1 = pos1
        self.posDim2 = pos2
        self.parent = None
        self.nodeType = 0
        self.neighboors = []
        
    def updateType(self,newType:int)->None:
        self.nodeType = newType
        
    def findTheoreticalDistanceToGoal(self,goal:object):
        return math.sqrt(math.pow(self.posDim1-goal.posDim1,2) + math.pow(self.posDim2 - goal.posDim2,2))
    
    # def addNeighboors(self,nodesAndNeighboors:tuple[list[object],list[list[object]]]):
    #     for node,neighboors in nodesAndNeighboors:
    #         self.addNeighboor(node)
    
    def addNeighboor(self,node:object):
        self.neighboors.append(node)
    
    def getNeighboors(self) -> list[object]:
        return self.neighboors
    
from Grid import *
import threading
import time
class Queue:
    def __init__(self):
        
        self.q = []
    
    #it's vice versa (worst -> best ). it's to reduce time complexity
    def bestEnque(self,element:object):
        self.q.append(element)
    
    def notBestEnque(self,element:object):
        self.q.insert(-1,element)
    
    def qNotEmpty(self)-> bool:
        if(len(self.q)>0):
            return True
        return False
            
    def bestDeque(self) -> object:
        return self.q.pop()
    
    
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
        self.q = Queue()
        self.startNode.findTheoreticalDistanceToGoal(self.endNode)
        self.startNode.addParent(self.startNode)
        self.q.bestEnque(self.startNode)
        
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
            time.sleep(0.02)
            currentNode:Node = self.q.bestDeque()
            if(not currentNode.isNotVisited()):
                continue
            if(currentNode == self.endNode):
                #self.grid.markAsBestWay(self.endNode.parent)
                break
            #print(f"x: {currentNode.posDim1}, y: {currentNode.posDim2}")
            nodesToGo = []
            for neighboor in currentNode.getNeighboors():
                
                # if(neighboor.isNotVisited() and neighboor.isNotObstacle()):
                if(neighboor.isNotObstacle()):
                    neighboor.findTheoreticalDistanceToGoal(self.endNode)
                    neighboor.findTheoreticalDistanceToStart(self.startNode)
                    #if(currentNode.valueToGoal>=neighboor.valueToGoal):
                    nodesToGo.append(neighboor)
                
            nodesToGo.sort(key=lambda x: x.valueToGoal,reverse=True)
                
            # we make algorithm faster if we sort parts of our main queue, so that best elements are always in the front
            # 11 is needed so that we don't lose link to our last
            # if len(self.q.q) > 4:
            #     nodesToGo.extend(self.q.q[0:3])  # Use extend to add elements from another list
            #     self.q.q.pop()
            #     self.q.q.pop()
            #     self.q.q.pop()
            #     nodesToGo.sort(key=lambda x: x.valueToGoal,reverse=True)#[0:len(currentNode.getNeighboors())-1]
            #     #self.q.q.append(nodesToGo.pop())
            #     #self.q.q.append(nodesToGo.pop())
            #     #self.q.q.append(nodesToGo.pop())
            # else:
            #     nodesToGo.sort(key=lambda x: x.valueToGoal,reverse=True)
                        
            #print(f"BEGIN \n ")
            for node in nodesToGo:
                #print(node.valueToGoal)
                node.addParent(currentNode)
                # if(self.q.qNotEmpty()):
                #     if(node.valueToGoal < self.q.q[-1].valueToGoal):
                #         self.q.bestEnque(node)
                #     else:
                #         self.q.notBestEnque(node)
                        
                # else:
                #     self.q.bestEnque(node)
                self.q.bestEnque(node)                
            #print(f"END \n")
            
            currentNode.setVisited()
            
                        
                        
                        
            
                
        
        
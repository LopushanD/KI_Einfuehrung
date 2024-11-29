import random
import heapq
class Queue:
    def __init__(self):
        
        self.q = []
    
    def enque(self,element):
        heapq.heappush(self.q,(element))
    
    
    def qNotEmpty(self)-> bool:
        if(len(self.q)>0):
            return True
        return False
            
    def deque(self) -> object:
        return heapq.heappop(self.q)
    
    def isInQueue(self,element:object) -> bool:
        if element in self.q:
            return True
        return False
    
def translateIndexesToPyGame(x:int,y:int,grid):
    """ translates coordinates from from user's point of view (0,0 is bottom left) to PyGame's point of view (0,0 is top left)
    coordinate entity is 1 tile, not 1 pixel. For example if tile is 10x10 pixels, then coordinate(3,3) is at (30,30) pixels 

    Args:
        x,y: coordinates from user's point of view (0,0 is bottom left)
        
    Returns coordinates from PyGame's point of view (0,0 is top left)
    """
    return (x-1,grid.sizeV//(grid.rectHeight+grid.margin)-y)

def setObstaclesRandomly(grid):
        """Very basic random obstacle generator. Can generate obstacles that block destination."""
        obstacleList =[]
        for i in range (2,round((grid.size[0]-1)/(grid.rectWidth+grid.margin)/1.3)):
                for j in range(2,round((grid.size[1]-1)/(grid.rectHeight+grid.margin))):
                        num = random.random()
                        if(num >0.85):

                            obstacleList.append((i,j,max(2,random.randint(i,i+3)),max(2,random.randint(j,j+3))))
        grid.setObstacles(obstacleList)
        
def getIndexesOfTile(x:int,y:int,field)->tuple[int,int]:
    """Takes position mouse cursor and returns index of corresponding tile under it. Recommended to use it with isPositionOnGrid() method, otherwise might lead to Out of Index Exception 

    Returns:
        tuple[int,int]: (horizontal index, vertical index)
    """
    
    index_x = getXIndexOfTile(x,field)
    index_y = getYIndexOfTile(y,field)
    return (index_x,index_y)

def getXIndexOfTile(x:int,field)->int:
    """Takes x coordinate and returns index x of corresponding tile under it. This method is not protected from Out of Index Exception 

    Returns:
        int: horizontal index
    """
    return max(0,(x-field.paddingH)//field.stepH )

def getYIndexOfTile(y:int,field)->int:
    """Takes y coordinate and returns index y of corresponding tile under it. This method is not protected from Out of Index Exception 

    Returns:
        int: vertical index
    """
    return max(0,(y-field.paddingV)//field.stepV )

def isPositionOnGrid(x:int,y:int,field)->bool:
    isOnGrid_x: bool = x>field.paddingH and x<field.paddingH+field.grid.sizeH
    isOnGrid_y: bool = y>field.paddingV and y<field.paddingV+field.grid.sizeV
    return isOnGrid_x and isOnGrid_y
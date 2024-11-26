import random
from Field import *
class Controller():
    """This class controlls all other classes. it is also program's entry point
    """
    def __init__(self):
        self.SPEED_SLOW=1
        self.SPEED_FAST=2
        self.SPEED_INSTANT=3
        
        self.field:Field = None
        self.grid:Grid = None
        self.algorithm:AStar = None
        
        self.terminateProgram = False
    #temporary dialog, replace it with GUI later
    def setGridSizeDialog(self)->None:
        print("Example of start/ end input: 10 10")
        start:list[str,str] = input("desired start position (default 1,1): -> ").split(" ")
        end:list[str,str] = input("desired end position (default 20,20): -> ").split(" ")
        print(f"{type(start)}")

        
        if(len(start)>1 and len(end)>1):
            start:tuple[int, int] = (int(start[0]),int(start[1]))
            end:tuple[int, int] = (int(end[0]),int(end[1]))
            gridHeight = int(input("desired grid height (default 500px): -> "))
            gridWidth = int(input("desired grid length (default 500px): -> "))
            rectHeight:int = int(input("desired cell height (default 20px): -> "))
            rectLength:int = int(input("desired cell length (default 20px): -> "))
            margin:int = int(input("desired margin between cells (default 2px): -> "))
            
            if gridHeight and gridWidth:
                self.grid = Grid(start,end,(gridWidth,gridHeight),rectLength,rectHeight,margin)
                self._setFieldSize(((gridWidth,gridHeight)))
            else:
                self.grid = Grid(start,end)
                self._setFieldSize((500,500))
        else:
            self.grid = Grid((1,1),(20,20))
            self._setFieldSize((500,500))
        
    #TEMPORARY DIALOG. MUST BE REWRITTEN WHEN GUI IS ADDED
    def setAnimationSpeedDialog(self):
        try:
            speed:int = int(input("Choose speed of animation: 1 - slow, 2 - fast, 3 - instant -> "))
            self.algorithm = AStar(self.grid,speed)
        except:
            self.algorithm = AStar(self.grid,self.SPEED_FAST)
    
    # # TEMPORARY. Rewrite it to real dialog. Make current code into random maze generator
    # def setAndClearObstaclesDialog(self):
    #     """User sees grid just like it will be in dialog. everything is drawn in real time (just like algorithm itself).
    #     User uses their mouse to create obstacles. It's done by clicking left mouse button over the grid and dragging the mouse.
    #     When right mouse button is clicked and mouse is being dragged, obstacles are removed.
    #     """
    #     # self.grid.setObstacles([]) #no obstacles at first
    #     pygame.mouse.set_visible(True)
    #     self.field.begin()
    #     # pygame.mouse.set_visible(False)
        
    
    def setObstaclesRandomly(self):
        """Very basic random obstacle generator. Can generate obstacles that block destination."""
        obstacleList =[]
        for i in range (2,round((self.grid.size[0]-1)/(self.grid.rectWidth+self.grid.margin)/1.3)):
                for j in range(2,round((self.grid.size[1]-1)/(self.grid.rectHeight+self.grid.margin))):
                        num = random.random()
                        if(num >0.85):

                            obstacleList.append((i,j,max(2,random.randint(i,i+3)),max(2,random.randint(j,j+3))))
        self.grid.setObstacles(obstacleList)
    
    def _setFieldSize(self,widthHeight:tuple[int,int])->None:
        w = round(widthHeight[0]*1.1)
        h = round(widthHeight[1]*1.1)
        self.field = Field((w,h))
        self.field.addGrid(self.grid)
    
    def begin(self):
        """start algorithm and it's visualization
        """
        algorithmThreadKiller = threading.Thread(target=self.killAlgorithmThread)
        algorithmThreadKiller.start()
        while not self.field.readyToStartAlgorithm:
            continue
        self.algorithm.start()
        
    
    def killAlgorithmThread(self):
        """Used for interrupting thread with A* algorithm. Otherwise it will run on the background until it finishes
        """
        while True:
            if self.field.done == True:
                self.algorithm.interruptThread()
                break
    
if __name__ == '__main__':
    # suited for terminal based UI, not for GUI
    game = Controller()
    game.setGridSizeDialog()
    game.setAnimationSpeedDialog()
    threading.Thread(target=game.begin).start()
    pygame.mouse.set_visible(True)
    game.field.begin()
    
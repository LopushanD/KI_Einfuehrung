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
                self.field = Field((gridWidth,gridHeight))
                self.grid = Grid(start,end,self.field.sizeH,self.field.sizeV,rectLength,rectHeight,margin)
                self.field.addGrid(self.grid)
            else:
                self.field = Field((500,750))
                self.grid = Grid(start,end,self.field.sizeH,self.field.sizeV)
                self.field.addGrid(self.grid)
        else:
            self.field = Field((585,585))
            self.grid = Grid((3,3),(3,18),round(self.field.sizeH*0.8),round(self.field.sizeV*0.8))
            self.field.addGrid(self.grid)
        
    #TEMPORARY DIALOG. MUST BE REWRITTEN WHEN GUI IS ADDED
    def setAnimationSpeedDialog(self):
        try:
            speed:int = int(input("Choose speed of animation: 1 - slow, 2 - fast, 3 - instant -> "))
            self.algorithm = AStar(self.grid,speed)
        except:
            self.algorithm = AStar(self.grid,self.SPEED_FAST)
    
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
    
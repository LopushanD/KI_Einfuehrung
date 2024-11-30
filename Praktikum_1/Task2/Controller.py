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
    #temporary dialog, replace it with GUI later
    def setGridSizeDialog(self)->None:
        """NEEDS CODE FIXES. this dialog should ask user what dimensions of grid and field he wants, but due to out of index bugs, values are hardcoded.
        """
        userInput = input("custom size? (No: just press enter \t Yes: input any character and press enter) -> ")
        if(len(userInput)>0):
            try:
                gridHeight = int(input("desired grid height (default 700px): -> "))
                
            except:
                gridHeight = 700
            try:
                gridWidth = int(input("desired grid length (default 700px): -> "))
                
            except:
                gridWidth = 700
        else:
            gridHeight = 700
            gridWidth = 700
        self.grid = Grid(gridWidth,gridHeight)
        self.field = Field(self.grid)
        # print(f"\t size(1) \t tile size(2) \t padding(3) \t margin(4) \t step(tilesize +margin)(5) \t length of grid(6)")
        # print(f"field: ({self.field.sizeH}, {self.field.sizeV})(1)\t --(2) \t ({self.field.paddingH} {self.field.paddingV})(3)\t --(4) \t ({self.field.stepH} {self.field.stepV})(5)\t --(6)")
        # print(f"grid: ({self.grid.sizeH}, {self.grid.sizeV})(1)\t ({self.grid.rectWidth} {self.grid.rectHeight})(2)\t --(3) \t {self.grid.margin}(4) \t --(5)\t ({len(self.grid.grid)} {len(self.grid.grid[0])})(6)")
        
    #TEMPORARY DIALOG. MUST BE REWRITTEN WHEN GUI IS ADDED
    def setAnimationSpeedDialog(self):
        try:
            speed:int = int(input("Choose speed of animation: 1 - slow, 2 - fast, 3 - instant -> "))
            self.algorithm = AStar(self.grid,speed)
        except:
            self.algorithm = AStar(self.grid,self.SPEED_FAST)
 
    def killOrRestartAlgorithmThread(self):
        """Used for interrupting thread with A* algorithm. Otherwise it will run on the background until it finishes
        """
        while True:
            # wait until user finishes with setting up
            while not self.field.readyToStartAlgorithm:
                continue
            # start/rerun thread. In case of rerunning, it cannot be done directly, so we need to create new instance
            oldSpeed = self.algorithm.algorithmSpeed
            self.algorithm = AStar(self.grid,self.SPEED_INSTANT) # speed here is just placeholder
            self.algorithm.algorithmSpeed = oldSpeed
            self.algorithm.start()
            # wait until user closes the window or resets everything
            while self.field.readyToStartAlgorithm and not self.field.endProgram:
                continue
            
            self.algorithm.interruptThread()
            if self.field.endProgram == True:
                break
            
if __name__ == '__main__':
    game = Controller()
    game.setGridSizeDialog()
    game.setAnimationSpeedDialog()
    algorithmThreadHandler = threading.Thread(target=game.killOrRestartAlgorithmThread)
    #configure this thread to be a daemon, so that it closes automatically when main thread is closed.
    algorithmThreadHandler.daemon = True
    algorithmThreadHandler.start()
    pygame.mouse.set_visible(True)
    game.field.begin()
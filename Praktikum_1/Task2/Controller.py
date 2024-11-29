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
        # userInput = input("custom size? (No: just press enter \t Yes: input any character and press enter)")
        
        # if(len(userInput)>0):
        #     gridHeight = int(input("desired grid height (default 700px): -> "))
        #     gridWidth = int(input("desired grid length (default 700px): -> "))
            
        #     if gridHeight:
        #         if gridWidth:
        #             self.field = Field((gridWidth,gridHeight))
        #         else:
        #             self.field = Field((700,gridHeight))
        #     elif gridWidth:
        #         self.field = Field((gridWidth,700))
        #     else:
        #         #user said yes to custom size, but didn't enter any dimensions
        #         self.field = Field((700,700))
        # else:
        #     self.field = Field((585,585))
        
        self.field = Field((585,585))
        self.grid = Grid(round(self.field.sizeH*0.8),round(self.field.sizeV*0.8))
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
    game = Controller()
    game.setGridSizeDialog()
    game.setAnimationSpeedDialog()
    threading.Thread(target=game.begin).start()
    pygame.mouse.set_visible(True)
    game.field.begin()
    
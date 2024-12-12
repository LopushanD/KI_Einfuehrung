from Field import *
from ConfigGUI import *
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
        self.configGUI:ConfigGUI = None
    #temporary dialog, replace it with GUI later
    
    def preparingParametersGUIDialog(self):
        """Set all parameters for field,grid and algorithm using GUI"""
        self.configGUI = ConfigGUI(self.field,self.grid,self.algorithm)
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
    game.preparingParametersGUIDialog()
    # game.setGridSizeDialog()
    # game.setAnimationSpeedDialog()
    algorithmThreadHandler = threading.Thread(target=game.killOrRestartAlgorithmThread)
    #configure this thread to be a daemon, so that it closes automatically when main thread is closed.
    algorithmThreadHandler.daemon = True
    algorithmThreadHandler.start()
    pygame.mouse.set_visible(True)
    game.field.begin()
from Field import *
from ConfigGUI import *
class Controller():
    """This class controlls all other classes. it is also program's entry point
    """
    def __init__(self):        
        self.field:Field = None
        self.grid:Grid = None
        self.algorithm:AStar = None
        self.configGUI:ConfigGUI = None
    #temporary dialog, replace it with GUI later
    
    def preparingParametersGUIDialog(self):
        """Set all parameters for field,grid and algorithm using GUI"""
        self.configGUI = ConfigGUI(self.field,self.grid,self.algorithm)
        self.field = self.configGUI.field
        self.grid = self.configGUI.grid
        self.algorithm = self.configGUI.algorithm
    def killOrRestartAlgorithmThread(self):
        """Used for interrupting thread with A* algorithm. Otherwise it will run on the background until it finishes
        """
        while True:
            # wait until user finishes with setting up
            while not self.field.readyToStartAlgorithm:
                continue
            # start/rerun thread. In case of rerunning, it cannot be done directly, so we need to create new instance
            oldSpeed = self.algorithm.pauseBetweenSteps
            self.algorithm = AStar(self.grid,1) # speed here is just placeholder
            self.algorithm.pauseBetweenSteps = oldSpeed
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
    try:
        game.field.pygame.mouse.set_visible(True)
    except:
        quit("seems like application was closed during configuration of parameters")
    # Algorithm runs in another background thread
    algorithmThreadHandler = threading.Thread(target=game.killOrRestartAlgorithmThread)
    # configure this thread to be a daemon, so that it closes automatically when main thread is closed.
    algorithmThreadHandler.daemon = True
    algorithmThreadHandler.start()
    game.field.begin()
from Field import *
class Controller():
    def __init__(self):
        
        # self.grid = Grid((1,1),(10,10),(400,400))
        # self.grid.setObstacles(None)
        # game = Field((600,1000))

        # game.addGrid(self.grid)
        # self.algorithm = AStar(self.grid)
        pass
        
    def setGridSizeDialog(self):
        pass
    
    def setAnimationSpeedDialog(self):
        pass
    
    def setAndClearObstaclesDialog(self):
        """User sees grid just like it will be in dialog. everything is drawn in real time (just like algorithm itself).
        User uses their mouse to create obstacles. It's done by clicking left mouse button over the grid and dragging the mouse.
        When right mouse button is clicked and mouse is being dragged, obstacles are removed.
        """
        pass
    
    def _setFieldSize(self):
        pass
    
    def begin(self):
        """start algorithm and it's visualization
        """
        pass
    
    
    
if __name__ == '__main__':
    # suited for terminal based UI, not for GUI
    game = Controller
    game.setGridSizeDialog()
    game.setAnimationSpeedDialog()
    game.setAndClearObstaclesDialog()
    game.begin()
    
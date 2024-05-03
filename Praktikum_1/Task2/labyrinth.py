from helperClasses import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

RECT_WIDTH = 20
RECT_HEIGHT = 20
MARGIN = 2

# ---
# Initialize your classes etc.here
# ---
"""
TO DO
        
        - make the field and grid dynamic (so that they work with different values)
        
        - stepV and stepH may be mixed up in some places, not a problem as long as we create square field
"""
obstaclesFromTo = [(16*(RECT_WIDTH+MARGIN),0*(RECT_HEIGHT+MARGIN),17*(RECT_WIDTH+MARGIN),9*(RECT_HEIGHT+MARGIN)),(4*(RECT_WIDTH+MARGIN),9*(RECT_HEIGHT+MARGIN),
                        11*(RECT_WIDTH+MARGIN),10*(RECT_HEIGHT+MARGIN)),(10*(RECT_WIDTH+MARGIN),10*(RECT_HEIGHT+MARGIN),11*(RECT_WIDTH+MARGIN),0*(RECT_HEIGHT+MARGIN))]
        
        
game = Field((500,500),RECT_HEIGHT+MARGIN,RECT_WIDTH+MARGIN)

grid = Grid((480,480),RECT_WIDTH,RECT_HEIGHT,MARGIN)
grid.addObstacles(obstaclesFromTo)
game.addGrid(grid)
game.run()

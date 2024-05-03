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
# x begin, y begin, x end, y end ; begin is including, end is excluding
obstaclesFromTo = [(5,10,11,10),(10,1,11,10),(2,2,4,3),(1,18,11,19)]
        
        
game = Field((500,500),RECT_HEIGHT+MARGIN,RECT_WIDTH+MARGIN)

grid = Grid((1,1),(19,19),(480,480),RECT_WIDTH,RECT_HEIGHT,MARGIN)
grid.setObstacles(obstaclesFromTo)
game.addGrid(grid)
print(grid.grid)
game.run()

from Field import *

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
        - implement addNeighboors(nodes,their neighboors ) function that calls addNeigboor for each neighboor for each node
        
        - make the field and grid dynamic (so that they work with different values)
        
        - stepV and stepH may be mixed up in some places, not a problem as long as we create square field
"""


# x begin, y begin, x end, y end ; begin is including, end is excluding
obstaclesFromTo = [(5,10,11,10),(10,0,11,15),(2,2,4,3),(1,18,11,19),(3,15,10,16),(2,3,6,9),(14,17,16,18),(13,3,14,19)]
# obstaclesFromTo = []
        
grid = Grid((1,1),(19,19),(500,500),RECT_WIDTH,RECT_HEIGHT,MARGIN)
grid.setObstacles(obstaclesFromTo)
        
game = Field((520,520),RECT_HEIGHT+MARGIN,RECT_WIDTH+MARGIN)


game.addGrid(grid)
searchAlg = AStar(grid)
#game.run()
# searchAlg.search()
searchAlg.start()
game.start()

#searchAlg.join()
#game.join()


# print(grid.grid[0][0])
#grid.markAsBestWay(grid.grid[grid.start[0]][grid.start[1]])

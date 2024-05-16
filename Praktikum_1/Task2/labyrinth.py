from Field import *


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
# obstaclesFromTo = [(3,8,15,9),(8,3,9,15)]
# obstaclesFromTo =[]
obstaclesFromTo = [(5,10,11,11),(10,1,11,11),(17,10,18,21)]
#obstaclesFromTo = [(5,10,11,10),(10,1,11,16),(2,2,4,3),(1,18,11,20),(3,15,10,16),(2,3,6,9),(14,17,16,18),(13,3,14,21)]
# obstaclesFromTo = [
#     (5, 10, 11, 11),   # Obstacle from (5, 10) to (10, 10)
#     (10, 1, 11, 17),   # Obstacle from (10, 1) to (10, 16)
#     (2, 2, 4, 4),      # Obstacle from (2, 2) to (3, 3)
#     (1, 18, 11, 21),   # Obstacle from (1, 18) to (10, 20)
#     (3, 15, 10, 17),   # Obstacle from (3, 15) to (9, 16)
#     (2, 3, 6, 10),     # Obstacle from (2, 3) to (5, 9)
#     (14, 17, 16, 19),  # Obstacle from (14, 17) to (15, 18)
#     (13, 3, 14, 22)    # Obstacle from (13, 3) to (13, 21)
# ]
# obstaclesFromTo = [
#     # First "L" shaped obstacle
#     (13, 1, 18, 20),  # Vertical part
#     (1, 10, 4, 11),  # Horizontal part
    
#     # Second inverted "L" shaped obstacle
#     (6, 18, 7, 21),  # Vertical part
#     (6, 6, 21, 17)   # Horizontal part
# ]
#           start   end    size
# grid = Grid((15,15),(18*2,18*2),(480*2,480*2),RECT_WIDTH//5,RECT_HEIGHT,MARGIN//5)
# grid.setObstacles(obstaclesFromTo)
# game = Field((500*2,500*2),(RECT_HEIGHT+MARGIN)//5,(RECT_WIDTH+MARGIN)//5)
        

grid = Grid((1,1),(20,20),(480,480),RECT_WIDTH,RECT_HEIGHT,MARGIN)
grid.setObstacles(obstaclesFromTo)
game = Field((500,500),RECT_HEIGHT+MARGIN,RECT_WIDTH+MARGIN)


game.addGrid(grid)
searchAlg = AStar(grid)

game.start()
searchAlg.start()

searchAlg.join()
game.join() 


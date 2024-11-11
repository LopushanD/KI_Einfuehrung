from Field import *
import random

RECT_WIDTH = 15
RECT_HEIGHT = 15
MARGIN = 2

# ---
# Initialize your classes etc.here
# ---
"""
TO DO
        
        - transform dialogs to GUI 
        
        - create random obstacle generator
                
        - Make the program work not only with square grid, but with rechtangular one too (where its height =/= its width)
        
"""


# x begin, y begin, x end, y end ; begin is including, end is excluding
# obstaclesFromTo = [(3,8,15,9),(8,3,9,15)]
# obstaclesFromTo =[]
# obstaclesFromTo = [(5,10,11,11),(10,1,11,11),(17,10,18,21)]
#obstaclesFromTo = [(5,10,11,10),(10,1,11,16),(2,2,4,3),(1,18,11,20),(3,15,10,16),(2,3,6,9),(14,17,16,18),(13,3,14,21)]
# obstaclesFromTo = [
#     (5, 10, 11, 11),   # Obstacle from (5, 10) to (10, 10)
#     (10, 1, 11, 17),   # Obstacle from (10, 1) to (10, 16)
#     (2, 2, 4, 4),      # Obstacle from (2, 2) to (3, 3)
#     (1, 18, 11, 21),   # Obstacle from (1, 18) to (10, 20)
#     (3, 15, 10, 17),   # Obstacle from (3, 15) to (9, 16)
#     (2, 3, 6, 10),     # Obstacle from (2, 3) to (5, 9)
#     (14, 17, 16, 19),  # Obstacle from (14, 17) to (15, 18)
#     (13, 3, 14, 22),    # Obstacle from (13, 3) to (13, 21)

#     (13, 1, 18, 20),  # Vertical part
# #     (1, 10, 4, 11),  # Horizontal part
    
#     # Second inverted "L" shaped obstacle
#     (6, 18, 7, 21),  # Vertical part
#     (6, 6, 21, 17)   # Horizontal part
# ]
#           start   end    size
# grid = Grid((15,15),(18*2,18*2),(480*2,480*2),RECT_WIDTH//5,RECT_HEIGHT,MARGIN//5)
# grid.setObstacles(obstaclesFromTo)
# game = Field((500*2,500*2),(RECT_HEIGHT+MARGIN)//5,(RECT_WIDTH+MARGIN)//5)

# GRID_WIDTH = 800
# GRID_HEIGHT = 800
# obstacleList =[]
# for i in range (2,round((GRID_WIDTH-1)/(RECT_WIDTH+MARGIN)/1.3)):
#         for j in range(2,round((GRID_HEIGHT-1)/(RECT_HEIGHT+MARGIN))):
#                 num = random.random()
#                 if(num >0.85):

#                         obstacleList.append((i,j,max(2,random.randint(i,i+3)),max(2,random.randint(j,j+3))))

# grid = Grid((1,1),(30,40),(GRID_WIDTH,GRID_HEIGHT),RECT_WIDTH,RECT_HEIGHT,MARGIN)
# grid.setObstacles(obstacleList)
# game = Field((1000,1000))


# game.addGrid(grid)
# searchAlg = AStar(grid)

# searchAlg.start()
# game.begin()

# searchAlg.join()
# game.join() 


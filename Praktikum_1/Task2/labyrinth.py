import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 2


# ---
# Initialize your classes etc.here
# ---
# class Grid:
#     def __init__(self):
#         pass
        
pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 14) # text font

# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, WHITE, BLACK)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (WIDTH//2,HEIGHT//2)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    
    # fill screen with black color
    screen.fill(BLACK)
    #render text
    #screen.blit(text, textRect)
    obstacleBegan = False
    obstaclesFromTo = [(16*(WIDTH+MARGIN),0*(HEIGHT+MARGIN),17*(WIDTH+MARGIN),9*(HEIGHT+MARGIN)),(4*(WIDTH+MARGIN),9*(HEIGHT+MARGIN),
                    11*(WIDTH+MARGIN),10*(HEIGHT+MARGIN)),(10*(WIDTH+MARGIN),10*(HEIGHT+MARGIN),11*(WIDTH+MARGIN),0*(HEIGHT+MARGIN))]
    for i in range(0,size[0],WIDTH+MARGIN):
        for j in range(0,size[1],HEIGHT+MARGIN):
            
            pygame.draw.rect(screen,WHITE,pygame.Rect(i,j,WIDTH,HEIGHT))
    
    for obstacle in obstaclesFromTo:
        print("wtf")
        pygame.draw.rect(screen,BLACK,pygame.Rect(obstacle[0],obstacle[1],abs(obstacle[0]-obstacle[2]),abs(obstacle[1]-obstacle[3])))
                # if((i,j) == (obstacle[0],obstacle[1])):
                #     obstacleBegan = True
                # if(obstacleBegan and (i,j) == (obstacle[2],obstacle[3])):
                #     obstacleBegan = False
            
    
    # ---
    # The code here ist called once per clock tick
    # Let your algorithm loop here
    # ---


            # ---
            # The screen is empty here
    # Put your 'drawing' code here
            #
            #   RECTANGEL EXAMPLE
            #
    #   The third Parameter defines the rectangles positioning etc: [y-pos,x-pos,width,height]
    #   pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * y + MARGIN,
    #                        (MARGIN + HEIGHT) * x + MARGIN,WIDTH,HEIGHT])
            # ---


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
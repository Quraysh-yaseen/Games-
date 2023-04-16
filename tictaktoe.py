import pygame ,sys

pygame.init() 

WIDTH = 600
HEIGHT = 600
LINE_WIDTH =15 

#RGB (RED,GREEN,BLUE)
RED =(255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23  ,145,135)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAK TOE')
screen.fill(BG_COLOR) 

#pygame.draw.line(screen,RED,(10,10),(300,300))

def draw_lines():
    # horizontal line
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200), LINE_WIDTH )
draw_lines()
#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
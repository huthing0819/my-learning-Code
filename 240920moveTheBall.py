import pygame,sys
pygame.init()
screen=pygame.display.set_mode([800,800])
screen.fill([255,255,255])
ball= pygame.image.load('Basketball.png')
x=50
y=50
x_speed = 10
y_speed =10
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,180,180],0)
    x+=x_speed
    y+=y_speed
    if x>screen.get_width()-180 or x<=0:
        x=-x_speed
    if y>screen.get_height()-180 or y<=0:
        y=-y_speed
    screen.blit(ball,[x,y])
    pygame.display.flip()
pygame.quit()

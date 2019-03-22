import pygame

pygame.init()
white=(255,255,255)

game_backgroud=pygame.display.set_mode((800,600))
pygame.display.set_caption("car")
clock=pygame.time.Clock()
carimage=pygame.image.load('blue.png')

def car(x,y):
    game_backgroud.blit(carimage,(x,y))

x=(800*0.45)
y=(600*0.8)

accident=False

while not accident:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            accident = True
    
    game_backgroud.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()

import pygame



pygame.init()
background = pygame.image.load("asset/bg.jpg")

pygame.display.set_caption("plant_vs_zombie")
pygame.display.set_mode((1024, 640))

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
class Player(pygame.sprite.Sprite):

    def

screen = pygame.display.set_mode((1024, 720))

running = True
while running:
    screen.blits(background, dest: (0, -200))
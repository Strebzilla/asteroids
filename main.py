# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    
    # Initialization
    
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Main game loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                     
        screen.fill("black")
        updateable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip() # Updates the contents of the display
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
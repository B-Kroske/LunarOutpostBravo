import pygame
import sys

from pygame.locals import *

from constants import *
from render import *

def init():
    pygame.init()
    surface = pygame.display.set_mode((1000,800))
    pygame.display.set_caption('Lunar Outpost Bravo')
    pygame.time.set_timer(USEREVENT+1, 1000)
    return surface

def main():
    seconds = 0
    surface = init()

    clock = pygame.time.Clock()

    render_screen(surface)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

from constants import *
from logger import log_state
import pygame
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    version = pygame.version.ver
    fps_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60)/1000
        #print(dt)
        
if __name__ == "__main__":
    main()

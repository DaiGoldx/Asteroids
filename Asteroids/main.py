from constants import *
from logger import log_state, log_event
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    version = pygame.version.ver
    fps_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroidField = AsteroidField()
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
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                 log_event("player_hit")
                 print("Game Over")
                 sys.exit()
        pygame.display.flip()
        dt = fps_clock.tick(60)/1000
        #print(dt)
        
if __name__ == "__main__":
    main()

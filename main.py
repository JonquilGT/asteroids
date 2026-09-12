from turtle import up, update
from logger import log_event
from asteroid import Asteroid
from player import Player
from shot import Shot
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroidfield import AsteroidField
import sys

def main():
    #Initialize pygame
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Setup clock to enable FPS limit
    clock = pygame.time.Clock()
    dt = 0.0

    #Build screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)

    #Build groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    #Build Player
    hero = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        updatable.update(dt)
        for asteroid in asteroids:
            if hero.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # print(dt)



if __name__ == "__main__":
    main()

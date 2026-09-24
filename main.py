import pygame

from asteroidfield import AsteroidField
from player import Player
from constants import *
from logger import log_state
from asteroid import Asteroid


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    asteroidfield = AsteroidField()


    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        updatable.update(dt)
        dt = clock.tick(60) / 1000
        pygame.display.flip()


        
        


if __name__ == "__main__":
    main()

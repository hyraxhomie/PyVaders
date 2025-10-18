import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    success, fail = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # assign groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # initialize
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    # gameloop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Game update logic
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Collision Check
        collision = False
        for item in asteroids:
            if item.collision(player):
                collision = True
                break
        if collision:
            break
        dt = clock.tick(60) / 1000

    print("Game over!")

if __name__ == "__main__":
    main()

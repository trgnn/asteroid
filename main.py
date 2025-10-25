import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# to run the game, use $ uv run main.py
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # 1) Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 2) Timing
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000

        # 3) Update (use dt)
        # updatable.update(dt)
        updatable.update(dt)

        # 4) Render
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()

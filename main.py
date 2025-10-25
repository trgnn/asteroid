import sys
import pygame
from constants import *
from player import Player
from shot import Shot
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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
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
        updatable.update(dt)
        for obj in asteroids:
            for bullet in shots:
                if bullet.collision(obj) == True:
                    obj.kill()
                    bullet.kill()
            if obj.collision(player) == True:
                print("Game over!")
                sys.exit()


        # 4) Render
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()

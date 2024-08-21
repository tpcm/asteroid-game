import pygame

from player import Player

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_KINDS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_SPAWN_RATE
    )

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")

        for to_update, to_draw in zip(updatable, drawable):
            to_update.update(dt=dt)
            to_draw.draw(screen=screen)

        pygame.display.flip()

        dt = pygame_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
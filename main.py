import pygame
import sys
from player import Player
from constants import *
from AsteroidField import AsteroidField
from asteroid import Asteroid
from shot import Shot

pygame.font.init()
font = pygame.font.Font(None, 36)

class GameManager:
    def __init__(self):
        self.score = 0

    def add_score(self, amount):
        self.score += amount
        print(f"Score updated! Current score: {self.score}")

    def asteroid_destroyed(self):
        self.add_score(1)

def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    pygame.init()
    
    game_manager = GameManager()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Shot.containers = shots_group, updatable, drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)

    updatable.add(player)
    drawable.add(player)
    
    Asteroid.containers = (asteroids, updatable, drawable, asteroids_group)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    game_loop(screen, updatable, drawable, player, asteroids, shots_group, asteroids_group, game_manager)
  
def game_loop(screen, updatable, drawable, player, asteroids, shots_group, asteroids_group, game_manager):
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable.update(dt=dt)

        # Render the score text
        score_text = font.render(f"Score: {game_manager.score}", True, (255, 255, 255))

        # Blit the score text at the top-left corner
        screen.blit(score_text, (10, 10))

        for sprite in drawable:
            sprite.draw(screen)

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        for asteroid in asteroids_group:
            for bullet in shots_group:
                if asteroid.collision(bullet):
                    asteroid.split(ASTEROID_MIN_RADIUS)
                    bullet.kill()
                    game_manager.asteroid_destroyed()
            
        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game over!")
                sys.exit()
    
if __name__ == "__main__":
    main()
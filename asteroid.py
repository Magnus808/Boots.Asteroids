import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Initialized with default value
        containers = None

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)

    def split(self, ASTEROID_MIN_RADIUS):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle1 = random.uniform(20, 50)
            angle2 = -angle1
        
            new_vector1 = self.velocity.rotate(angle1)
            new_vector2 = self.velocity.rotate(angle2)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            faster_vector1 = new_vector1 * 1.2
            faster_vector2 = new_vector2 * 1.2

            Asteroid(self.position.x, self.position.y, new_radius).velocity = faster_vector1
            Asteroid(self.position.x, self.position.y, new_radius).velocity = faster_vector2
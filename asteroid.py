import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = (255,255,255)
        asteroid = pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if self.radius >= ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            first_vector = self.velocity.rotate(new_angle)
            second_vector = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first_vector*1.2
            second_asteroid.velocity = second_vector*1.2

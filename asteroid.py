import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius) 


    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid_angle_one = self.velocity.rotate(random_angle)
            asteroid_angle_two = self.velocity.rotate(-random_angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_one.velocity = asteroid_angle_one * 1.2
            asteroid_two.velocity = asteroid_angle_two * 1.2
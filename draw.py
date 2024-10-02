import pygame
import math
import sys

class Pend:
    def __init__(self, thread_length, pendulum_angle, pendulum_mass) -> None:
        pygame.init()

        self.screen_size = (500, 500)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bg_color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        
        self.center_x, self.center_y = self.screen_size[0] // 2, self.screen_size[1] // 4
        self.length = thread_length 
        self.radius = 20 
        self.angle = pendulum_angle
        self.angular_velocity = 0
        self.angular_acceleration = 0
        self.gravity = 0.01
        self.mass = pendulum_mass

        self.run_sim()

    def draw_pendulum(self):
        x = self.center_x + self.length * math.sin(self.angle)
        y = self.center_y + self.length * math.cos(self.angle)

        top_point = (self.center_x, self.center_y)
        bottom_point = (x, y)

        self.screen.fill(self.bg_color)
        pygame.draw.line(self.screen, (0, 0, 0), top_point, bottom_point, 2)
        pygame.draw.circle(self.screen, (0, 0, 0), (int(x), int(y)), self.radius)

    def update_physics(self):
        self.angular_acceleration = (-self.gravity / self.length) * math.sin(self.angle)

        damping = 0.99 - (0.001 * self.mass)
        self.angular_velocity += self.angular_acceleration 
        self.angle += self.angular_velocity 

        self.angular_velocity *= damping

    def run_sim(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_physics()
            self.draw_pendulum()

            pygame.display.flip()
            self.clock.tick(60)

    
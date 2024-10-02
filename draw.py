import pygame
import pymunk
import sys

class Pend:
    def __init__(self) -> None:
        pygame.init()

        screen_size = (500, 500)
        screen = pygame.display.set_mode(screen_size)
        bg_color = (255, 255, 255)
        screen.fill(bg_color)
        
        center_x, center_y = screen_size[0] // 2, screen_size[1] // 2
        
        top_point = (center_x, center_y - 100)
        bottom_point = (center_x, center_y + 100)

        circle_radius = 20
        
        screen.fill(bg_color)

        pygame.draw.line(screen, (0, 0, 0), top_point, bottom_point, 2)
        pygame.draw.circle(screen, (0, 0, 0), bottom_point, circle_radius)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.flip()
    
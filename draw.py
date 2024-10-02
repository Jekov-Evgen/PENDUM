import pygame
import sys

class Pend:
    def __init__(self) -> None:
        pygame.init()

        screen = pygame.display.set_mode((500, 500))
        bg_color = (255, 255, 255)
        screen.fill(bg_color)
        line = pygame.draw.line(screen, (0, 0, 0), [100, 100], [200, 200], 1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
    
import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    x = 0
    y = 0
    z = 0

    while True:
        # TODO 4: Set the clock speed to 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # DONE 3: Make the eye pupils move with Up, Down, Left, and Right keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            y -= 1
        if pressed_keys[pygame.K_DOWN]:
            y += 1
        if pressed_keys[pygame.K_LEFT]:
            x -= 1
        if pressed_keys[pygame.K_RIGHT]:
            x += 1
        if pressed_keys[pygame.K_z]:
            z += 0.8
        if pressed_keys[pygame.K_x]:
            z -= 0.8
        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242+x, 162+y), 7+z)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398+x, 162+y), 7+z)  # black pupil

        # DONE 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        pygame.draw.circle(screen, (80, 0, 0), (320, 245), 10)
        # DONE 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))
        pygame.display.update()


main()

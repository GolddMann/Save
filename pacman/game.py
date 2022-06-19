import pygame


if __name__ == "__main__":
    size = width, height = 400, 500
    pygame.init()
    screen = pygame.display.set_mode(size)
    image = pygame.image.load("103800.png")

    while True:
        for event in pygame.event.get():
            if event:
                pygame.quit()
                exit(0)

        pygame.display.update()

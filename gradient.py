import pygame

# Window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

### initialisation
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Gradient Rect")


def gradientRect(window, leftTop, leftBottom, rightTop, rightBottom, targetRect):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    surface = pygame.Surface((2, 2))
    pygame.draw.rect(surface, leftTop, (0, 0, 1, 1))
    pygame.draw.rect(surface, leftBottom, (0, 1, 1, 1))
    pygame.draw.rect(surface, rightTop, (1, 0, 1, 1))
    pygame.draw.rect(surface, rightBottom, (1, 1, 1, 1))
    surface = pygame.transform.smoothscale(
        surface, (targetRect.width, targetRect.height)
    )
    window.blit(surface, targetRect)


gradientRect(
    window,
    (255, 255, 255),
    (0, 0, 0),
    (255, 0, 0),
    (0, 0, 0),
    pygame.Rect(40, 40, 256, 256),
)
pygame.display.update()
### Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the window


pygame.quit()

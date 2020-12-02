import pygame
from const import BLACK, WIDTH, HEIGHT, to_rgb, WHITE


class Widget:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xBound = (self.x, self.x + self.width)
        self.yBound = (self.y, self.y + self.height)
        self.bbox = pygame.Rect(
            self.xBound[0] - 10, self.y - 10, self.width + 20, self.height + 20
        )

    def clicked(self, x, y):
        topleft = self.bbox.topleft
        botright = self.bbox.bottomright
        return topleft[0] <= x <= botright[0] and topleft[1] <= y <= botright[1]

    def update(self):
        pygame.display.update(self.bbox)


class SliderWidget(Widget):
    def __init__(self):
        super().__init__((WIDTH - 360) // 2, HEIGHT - 50, 360, 10)

    def draw(self, win):
        x = 0
        for h in range(360):
            pygame.draw.rect(win, to_rgb(h, 255, 255), (self.x + x, self.y, 3, 3))
            x += 1


class GradientWidget(Widget):
    def __init__(self):
        super().__init__(30, 30, 256, 256)

    def draw(self, win, color):
        bd = 3
        pygame.draw.rect(
            win,
            WHITE,
            (self.x - bd, self.y - bd, self.width + bd * 2, self.height + bd * 2),
        )
        surface = pygame.Surface((2, 2))
        pygame.draw.rect(surface, WHITE, (0, 0, 1, 1))
        pygame.draw.rect(surface, BLACK, (0, 1, 1, 1))
        pygame.draw.rect(surface, color, (1, 0, 1, 1))
        pygame.draw.rect(surface, BLACK, (1, 1, 1, 1))
        target = pygame.Rect(30, 30, self.width, self.height)
        surface = pygame.transform.smoothscale(surface, (self.width, self.height))
        win.blit(surface, target)

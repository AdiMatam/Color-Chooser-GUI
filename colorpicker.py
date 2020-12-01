import pygame
from pygame.constants import (
    KEYDOWN,
    K_x,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    QUIT,
    K_9,
    K_0,
)
from pygame.font import SysFont
from fxns import to_rgb, to_hex, to_hsv

WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# txt = font.render("hello", True, (0, 0, 0))
# win.blit(txt, (150, 200))


class SliderStruct:
    def __init__(self, y):
        self.xPad = (WIDTH - 360) // 2
        self.xBound = [self.xPad, self.xPad + 360]
        self.set_y(y)

    def set_y(self, y):
        self.y = y
        self.bbox = pygame.Rect(self.xBound[0] - 20, y - 10, self.xBound[1] + 20, 25)

    def clicked(self, x, y):
        topleft = self.bbox.topleft
        botright = self.bbox.bottomright
        return topleft[0] <= x <= botright[0] and topleft[1] <= y <= botright[1]


class ColorPicker:
    def __init__(self, win, hue=0):
        self.win = win
        self.font = SysFont("calibri", 16)
        self.hue = hue
        self.slider = SliderStruct(HEIGHT - 50)
        self.draw_slider()

    def draw_slider(self):
        for h in range(360):
            self.circle(h + self.slider.xPad, self.slider.y, to_rgb(h, 255, 255), 1)
        circleX = self.slider.xPad + self.hue
        self.circle(circleX, self.slider.y, WHITE, 10)
        self.circle(circleX, self.slider.y, to_rgb(self.hue, 255, 255), 8)
        self.draw_gradient()
        self.draw_preview()
        self.update()

    def draw_preview(self):
        pass

    def draw_gradient(self):
        x = y = 30
        bd = 3
        size = 256
        pygame.draw.rect(
            self.win, WHITE, (x - bd, y - bd, size + bd * 2, size + bd * 2)
        )
        target = pygame.Rect(30, 30, size, size)
        extreme = to_rgb(self.hue, 255, 255)

        surface = pygame.Surface((2, 2))
        pygame.draw.rect(surface, WHITE, (0, 0, 1, 1))
        pygame.draw.rect(surface, BLACK, (0, 1, 1, 1))
        pygame.draw.rect(surface, extreme, (1, 0, 1, 1))
        pygame.draw.rect(surface, BLACK, (1, 1, 1, 1))
        surface = pygame.transform.smoothscale(surface, (target.width, target.height))
        self.win.blit(surface, target)

    def circle(self, x: int, y: int, color: tuple, radius: int):
        pygame.draw.circle(self.win, color, (x, y), radius)

    def update(self, rect=None):
        if not rect:
            pygame.display.update()
        else:
            pygame.display.update(rect)

    def __call__(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif pygame.mouse.get_pressed()[0]:
                    self.win.fill(BLACK)
                    mx, my = pygame.mouse.get_pos()
                    if self.slider.clicked(mx, my):
                        mx = max(mx, self.slider.xBound[0])
                        mx = min(mx, self.slider.xBound[1])
                        self.hue = mx - self.slider.xPad
                        self.draw_slider()
                elif event.type == KEYDOWN:
                    print(event.unicode)
        return


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
picker = ColorPicker(win)
picker()
pygame.quit()


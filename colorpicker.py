from re import split

import pygame
from pygame.constants import KEYDOWN, QUIT
from pygame.font import SysFont

from const import *
from textmanage import TextManager
from widgets import GradientWidget, PreviewWidget, SliderWidget


class ColorPicker:
    def __init__(self, win, hue=0):
        # PYGAME
        self.win = win
        self.font = SysFont("calibri", 24, bold=True)

        # COLOR VALUES
        self.hue = hue
        self.sat = 255
        self.val = 255
        self.bounds = (359, 255, 255)

        # WIDGETS
        self.slider = SliderWidget()
        self.gradient = GradientWidget()
        self.preview = PreviewWidget()
        self.input = TextManager(f"HSV: {self.hue},{self.sat},{self.val}")

        self.draw_all()

    def draw_all(self):
        self.draw_slider()
        self.draw_gradient()
        self.draw_preview()

    def draw_slider(self):
        self.slider.draw(self.win)
        circleX = self.slider.x + self.hue
        self.circle(circleX, self.slider.y + 2, DOT, BBOX)
        self.circle(circleX, self.slider.y + 2, to_rgb(self.hue, 255, 255), BBOX - 2)
        self.slider.update()
        self.draw_gradient()

    def draw_gradient(self):
        self.gradient.draw(self.win, self.hue)
        circleX = self.gradient.x + self.sat
        circleY = self.gradient.y - self.val + 255
        self.circle(circleX, circleY, DOT, BBOX)
        self.circle(circleX, circleY, to_rgb(self.hue, self.sat, self.val), BBOX - 2)
        self.gradient.update()
        self.draw_preview()

    def draw_preview(self, external=False):
        self.preview.draw(self.win, to_rgb(self.hue, self.sat, self.val))
        if not external:
            self.input.set_text(f"HSV: {self.hue},{self.sat},{self.val}")
        self.draw_text()
        self.preview.update()

    def draw_text(self):
        if self.val > 255 // 2:
            rnd = self.font.render(str(self.input), True, BLACK)
        else:
            rnd = self.font.render(str(self.input), True, WHITE)
        rect = rnd.get_rect()
        x = self.preview.x + self.preview.width // 2 - rect.width // 2
        y = self.preview.y + self.preview.height // 2 - rect.height // 2
        self.win.blit(rnd, (x, y))

    def circle(self, x: int, y: int, color: tuple, radius: int):
        pygame.draw.circle(self.win, color, (x, y), radius)

    def set_vals(self, vals: list) -> None:
        for i in range(3):
            vals[i] = max(0, vals[i])
            vals[i] = min(vals[i], self.bounds[i])
        self.hue, self.sat, self.val = vals

    def __call__(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif pygame.mouse.get_pressed()[0]:
                    self.win.fill(WHITE)
                    mx, my = pygame.mouse.get_pos()
                    if self.slider.clicked(mx, my):
                        mx = max(mx, self.slider.xBound[0])
                        mx = min(mx, self.slider.xBound[1])
                        self.hue = min(359, mx - self.slider.x)
                        self.draw_slider()
                    elif self.gradient.clicked(mx, my):
                        mx = max(mx, self.gradient.xBound[0])
                        mx = min(mx, self.gradient.xBound[1] - 1)
                        self.sat = mx - self.gradient.x
                        my = max(my, self.gradient.yBound[0])
                        my = min(my, self.gradient.yBound[1] - 1)
                        self.val = self.gradient.y + 255 - my
                        self.draw_gradient()
                elif event.type == KEYDOWN:
                    try:
                        char = event.unicode
                        code = ord(char)
                        if code == 8:
                            del self.input[-1]
                            self.draw_preview(external=True)
                        elif code == 13 and PATTERN.match(self.input[5:]):
                            hsv = [int(num) for num in split(DELIMS, self.input[5:])]
                            self.set_vals(hsv)
                            self.draw_slider()
                        elif code != 32:
                            self.input.append(char)
                            self.draw_preview(external=True)
                    except:
                        continue
        return


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(WHITE)
pygame.display.update()
picker = ColorPicker(win)
picker()
pygame.quit()


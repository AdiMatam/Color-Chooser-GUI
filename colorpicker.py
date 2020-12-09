import pygame
from pygame.constants import KEYDOWN, QUIT
from pygame.font import SysFont
from const import *
from widgets import SliderWidget, GradientWidget


class ColorPicker:
    def __init__(self, win, hue=0):
        self.win = win
        self.font = SysFont("calibri", 24, bold=True)
        self.hue = hue
        self.sat = 255
        self.val = 255
        self.input = ""
        self.slider = SliderWidget()
        self.gradient = GradientWidget()
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
        self.gradient.draw(self.win, to_rgb(self.hue, 255, 255))
        circleX = self.gradient.x + self.sat
        circleY = self.gradient.y - self.val + 255
        self.circle(circleX, circleY, DOT, BBOX)
        self.circle(circleX, circleY, to_rgb(self.hue, self.sat, self.val), BBOX - 2)
        self.gradient.update()
        self.draw_preview()

    def draw_preview(self):
        r, g, b = to_rgb(self.hue, self.sat, self.val)
        hexx = to_hex(r, g, b)
        texts = [
            f"HEX: {hexx}",
            f"RGB: {r}, {g}, {b}",
            f"HSV: {self.hue}, {self.sat}, {self.val}",
        ]
        y = 150
        for text in texts:
            rnd = self.font.render(text, True, BLACK)
            win.blit(rnd, (400, y))
            y += 30
        pygame.display.update(pygame.Rect(350, 130, 250, 120))

    def circle(self, x: int, y: int, color: tuple, radius: int):
        pygame.draw.circle(self.win, color, (x, y), radius)

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
                        key = ord(event.unicode)
                        if key == 8:
                            print(ERASE, end="")
                            self.input = self.input[:-1]
                        elif key == 13:
                            print("")
                            self.input = ""
                        else:
                            self.input += event.unicode
                        print(self.input, end="\r")
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


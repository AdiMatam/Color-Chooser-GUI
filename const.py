WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BBOX = 12


def to_rgb(h, s, v):
    if s == 0:
        return (v, v, v)

    s /= 255
    h /= 60
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    if i == 0:
        r = v
        g = t
        b = p
    elif i == 1:
        r = q
        g = v
        b = p
    elif i == 2:
        r = p
        g = v
        b = t
    elif i == 3:
        r = p
        g = q
        b = v
    elif i == 4:
        r = t
        g = p
        b = v
    else:
        r = v
        g = p
        b = q
    return (int(r), int(g), int(b))


def to_hsv(r, g, b):
    mn = min(r, min(g, b))
    mx = max(r, max(g, b))
    v = mx
    delta = mx - mn
    if mx != 0:
        s = (delta / mx) * 256
    else:
        s = 0
        h = -1
        return (h, s, v)
    if r == mx:
        h = (g - b) / delta
    elif g == mx:
        h = (b - r) / delta
        h += 2
    else:
        h = (r - g) / delta
        h += 4
    h *= 60
    if h < 0:
        h += 360

    return (int(h), int(s), int(v))


def to_hex(r, g, b):
    color = "#"
    for c in (r, g, b):
        color += format(c, "02x")
    return color

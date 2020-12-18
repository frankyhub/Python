"""
LED dance
========= mu =========="""

import microbit
import random

def led_dance(delay):
    dots = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
    while True:
        dots[random.randrange(5)][random.randrange(5)] = 8
        for i in range(5):
            for j in range(5):
                microbit.display.set_pixel(i, j, dots[i][j])
                dots[i][j] = max(dots[i][j] - 1, 0)
        microbit.sleep(delay)

led_dance(100)

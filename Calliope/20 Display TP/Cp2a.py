"""
Display Pixel ansteuern

========= TigerJython =========="""
from calliope_mini import *

for x in range(5):
    display.set_pixel(x, 2, 9)
    sleep(400)
    display.set_pixel(x, 2, 0)


"""
Display Pixel ansteuern

========= TigerJython =========="""
from calliope_mini import *

for i in range(3):
    display.show(Image.ARROW_N)
    sleep(1000)
    display.show(Image.ARROW_E)
    sleep(1000)
    display.show(Image.ARROW_S)
    sleep(1000)
    display.show(Image.ARROW_W)
    sleep(1000)
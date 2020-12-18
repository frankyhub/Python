"""
Display Pixel ansteuern

========= TigerJython =========="""
from calliope_mini import *
from random import randint

def randomLed():
    display.clear()
    x = randint(0, 4)
    y = randint(0, 4)    
    display.set_pixel(x, y, 9)

while True:
    randomLed()
    sleep(200)        
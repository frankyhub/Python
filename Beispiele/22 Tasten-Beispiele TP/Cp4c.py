"""
Tasten Beispiel

========= TigerJython =========="""
from calliope_mini import *

def blink(x, y):
    display.set_pixel(x, y, 9)
    sleep(1000)    
    display.set_pixel(x, y, 0)
    sleep(1000)    

while True:
    if button_a.was_pressed():
        display.show(Image.SQUARE)
        sleep(1000)
        display.clear()
    blink(2, 2)
    
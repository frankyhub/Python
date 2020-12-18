"""
Tasten Beispiel

========= TigerJython =========="""
from calliope_mini import *

while True:
    if button_a.was_pressed():
        display.clear()
        display.show(Image.NO)
        sleep(1000)
        
    for y in range(5):
        for x in range(5):
            display.clear() 
            display.set_pixel(x, y, 9)
            sleep(100)
   





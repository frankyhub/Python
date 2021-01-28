from calliope_mini import *

def blink(x, y):
    display.set_pixel(x, y, 9)
    sleep(500)    
    display.set_pixel(x, y, 0)
    sleep(500)    

while True:
    if button_a.is_pressed():
        blink(0, 2)
    if button_b.is_pressed():
        blink(4, 2)
    

 
""" TigerJyton    
    Taster -> LED ein/aus    
=================================================
"""

from calliope_mini import *

def blink(x, y):
    display.set_pixel(x, y, 9)
    sleep(300)    
    display.set_pixel(x, y, 0)
    sleep(5)    

while True:
    if button_a.is_pressed():
        blink(0, 2)
    sleep(10) 
    if button_b.is_pressed():
        blink(4, 2)
    sleep(10)
    
    if pin0.read_digital():
        display.set_pixel(0, 3, 9)
    else: 
        display.set_pixel(0, 3, 0)  
    sleep(100)    
 
    if pin1.read_digital():
        display.set_pixel(1, 4, 9)
    else: 
        display.set_pixel(1, 4, 0)   
    sleep(100)
    
    if pin2.read_digital():
        display.set_pixel(3, 4, 9)
    else: 
        display.set_pixel(3, 4, 0)   
    sleep(100)
    
    if pin3.read_digital():
        display.set_pixel(4, 3, 9)
    else: 
        display.set_pixel(4, 3, 0)
    sleep(100)
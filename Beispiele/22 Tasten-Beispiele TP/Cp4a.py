"""
Tasten Beispiel

========= TigerJython =========="""
from calliope_mini import *
t = 0
def blink(x, y):
    display.set_pixel(x, y, 9)
    sleep(300)    
    display.set_pixel(x, y, 0)
    sleep(300)    

while True:
    if button_a.is_pressed():
        blink(0, 2)
    sleep(10) 
    if button_b.is_pressed():
        blink(4, 2)
    sleep(10)
    
    if pin0.read_digital():
        blink(0, 3)   
    sleep(100)    
 
    if pin1.read_digital():
        blink(1, 4)   
    sleep(100)
    
    if pin2.read_digital():
        blink(3, 4)   
    sleep(100)
    
    if pin3.read_digital():
        blink(4, 3)   
    sleep(100)
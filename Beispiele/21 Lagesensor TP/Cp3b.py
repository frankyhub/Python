"""
Accelerometer mit Accel_x Accel_y simulieren

========= TigerJython =========="""
from calliope_mini import *

x = 2
y = 2

while True:
    accX = accelerometer.get_x()
    accY = accelerometer.get_y() 
    if accX > 10 and y > 0:
        y -= 1
    elif accX < -10 and y < 4:
        y += 1
    elif accY < -10 and x < 4:
        x += 1
    elif accY > 10 and x > 0:
        x -= 1
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(200)
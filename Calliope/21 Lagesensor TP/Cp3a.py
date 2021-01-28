"""
Accelerometer mit Accel_x simulieren

========= TigerJython =========="""
from calliope_mini import *

while True:
    acc = accelerometer.get_x()
    print (acc)
    if acc > 0:
        display.show(Image.ARROW_N)
    else:
        display.show(Image.ARROW_S)
    sleep(100)  


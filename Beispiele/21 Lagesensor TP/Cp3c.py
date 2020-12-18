from calliope_mini import *
from cputils import *

while True:
    a = accelerometer.get_values()
    roll = getRoll(a)
    print(roll)
    if roll >= 0:
        display.show(Image.ARROW_N)
    if roll <= 0:
        display.show(Image.ARROW_S)
    sleep(0.3)

    


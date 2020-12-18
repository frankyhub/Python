"""
LED blinken lassen (digitalio)

============ mu =========="""

import time
import digitalio
import board

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

while True:
    # turn led ON
    led.value = True
    # wait 1 second
    time.sleep(1.0)
    # turn led off
    led.value = False
    # wait 1 second
    time.sleep(1.0)

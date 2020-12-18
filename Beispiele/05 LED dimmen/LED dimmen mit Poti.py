"""
LED dimmen mit Poti

========== mu ==========="""
import time
import digitalio
import analogio
import board

LED = digitalio.DigitalInOut(board.D13)
LED.switch_to_output()
POT = analogio.AnalogIn(board.A0)

SENSOR_VAL = 0

while True:
    # Poti Wert/max Poti Wert
    SENSOR_VAL = POT.value / 65536
    print(SENSOR_VAL)
    LED.value = True
    time.sleep(SENSOR_VAL)
    LED.value = False
    time.sleep(SENSOR_VAL)

"""
Alarm, wenn TEMP einen Schwellenwert überschreitet

================================================="""

import time
import analogio
import pulseio
import board
from simpleio import map_range

PIEZO = pulseio.PWMOut(board.D8, frequency=440, duty_cycle=0, variable_frequency=True)
TMP_36 = analogio.AnalogIn(board.A0)

FREEZING_TEMP = 0
BOIL_TEMP = 100

while True:
    TEMP = map_range(TMP_36.value, 0, 65535, 0, 5)
    # Temperatur in Grad C
    TEMP = (TEMP - .5) * 100
    print(TEMP)

    if TEMP < FREEZING_TEMP:
        PIEZO.duty_cycle = 30000
    if TEMP > BOIL_TEMP:
        PIEZO.duty_cycle = 10000
    time.sleep(.5)

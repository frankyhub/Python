"""
Temperatur-Anzeige

================================================="""

import time
import analogio
import board
from simpleio import map_range

TEMP_SENSOR = analogio.AnalogIn(board.A0)


def get_voltage(_temp_sensor):
    """erhält die Spannung des TMP36."""
    voltage_val = map_range(_temp_sensor.value, 0, 65535, 0, 3.3)
    return voltage_val


while True:
    TMP = get_voltage(TEMP_SENSOR)
    print("Voltage =", TMP, end="")
    # Konvertierung in Grad C
    TMP = (TMP - 0.5) * 100
    print("   Temperature =", TMP)
    time.sleep(1)
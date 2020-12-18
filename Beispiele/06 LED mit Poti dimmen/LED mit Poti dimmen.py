"""
LED mit Poti dimmen

========== mu ================"""

import analogio
import board
import pulseio

led = pulseio.PWMOut(board.D9)
pot = analogio.AnalogIn(board.A0)

while True:
    led.duty_cycle = pot.value

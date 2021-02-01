#https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/all
#Funkt
#UNO 32
"""PWM
"""

import machine
import sys
import utime

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
repl_led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
pwm_pin = machine.Pin(27, machine.Pin.OUT)

# Create a PWM object out of our pin object
pwm = machine.PWM(pwm_pin)

# Slowly fade LED brightness
while True:

    # If button 0 is pressed, turn on LED and drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        repl_led.value(1)
        sys.exit()

    # Increase brightness of LED if button is held
    for i in range(1024):
        if button.value() == 0:
            pwm.duty(i)
            utime.sleep_ms(2)
        else:
            pwm.duty(0)

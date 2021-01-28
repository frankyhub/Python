"""
Taster->LED

================================================="""
import digitalio
import board

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
button = digitalio.DigitalInOut(board.D2)
button.switch_to_input()


while True:
    btn_state = button.value
    led.value = not btn_state
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/all

#Intere LED EIN:
import machine
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

#Intere LED AUS:
import machine
led = machine.Pin(2, machine.Pin.OUT)
led.value(0)
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Blink int LED PIN2
Programm Stopp mit PIN0, dann Dropping to REPL in der Kommandozeile

import machine
import sys
import utime

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(2, machine.Pin.OUT)

# Blink forever
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    # Turn LED on and then off
    led.value(1)
    utime.sleep_ms(500)
    led.value(0)
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Int LED heller dimmen, wenn PIN0 = 0
import machine
import sys
import utime

# Pin definitions
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
pwm_pin = machine.Pin(2, machine.Pin.OUT)

# Create a PWM object out of our pin object
pwm = machine.PWM(pwm_pin)

# Slowly fade LED brightness
while True:
    # Increase brightness of LED if button is held
    for i in range(1024):
        if button.value() == 0:
            pwm.duty(i)
            utime.sleep_ms(2)
            
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
### Am Analogeingang GPIO39 (unten li, USB oben) Poti anschließen, der Spannungswert wird in der Kommandozeile angezeigt
import machine
import sys
import utime

# Pin definitions

adc_pin = machine.Pin(39)

# Create an ADC object out of our pin object
adc = machine.ADC(adc_pin)

# 11 dB attenuation means full 0 - 3.3V range
adc.atten(adc.ATTN_11DB)

# Blink forever
while True:


    # Read ADC and convert to voltage
    val = adc.read()
    val = val * (3.3 / 4095)
    print(round(val, 2), "V")

    # Wait a bit before taking another reading
    utime.sleep_ms(100)
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Test mit TMP102 temperature sensor Adresse 0x48      tmp102_addr = 0x48
I2C Test BME zeigt 0 an
import machine
import sys
import utime

###############################################################################
# Parameters and global variables

# Pin definitions
#repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
repl_led = machine.Pin(2, machine.Pin.OUT)
sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

# Create an I2C object out of our SDA and SCL pin objects
i2c = machine.I2C(sda=sda_pin, scl=scl_pin)

# BME address on the I2C bus
tmp102_addr = 0x76

# TMP102 register addresses
reg_temp = 0x00
reg_config = 0x01

###############################################################################
# Functions

# Calculate the 2's complement of a number
def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val

# Read temperature registers and calculate Celsius
def read_temp():

    # Read temperature registers
    val = i2c.readfrom_mem(tmp102_addr, reg_temp, 2)
    temp_c = (val[0] << 4) | (val[1] >> 5)

    # Convert to 2s complement (temperatures can be negative)
    temp_c = twos_comp(temp_c, 12)

    # Convert registers value to temperature (C)
    temp_c = temp_c * 0.0625

    return temp_c

# Initialize communications with the TMP102
def init():

    # Read CONFIG register (2 bytes) and convert to integer list
    val = i2c.readfrom_mem(tmp102_addr, reg_config, 2)
    val = list(val)

    # Set to 4 Hz sampling (CR1, CR0 = 0b10)
    val[1] = val[1] & 0b00111111
    val[1] = val[1] | (0b10 << 6)

    # Write 4 Hz sampling back to CONFIG
    i2c.writeto_mem(tmp102_addr, reg_config, bytearray(val))

###############################################################################
# Main script

# Print out temperature every second
while True:

    # Read temperature and print it to the console
    temperature = read_temp()
    print(round(temperature, 2), "C")
    utime.sleep(1)

""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#WLAN Connect funkt
import machine
import sys
import network
import utime
import urequests

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
repl_led = machine.Pin(2, machine.Pin.OUT)

# Network settings
wifi_ssid = "R2-D2"
wifi_password = "2QK384JVPX"

# Web page (non-SSL) to get
url = "http://example.com"

# Create a station object to store our connection
station = network.WLAN(network.STA_IF)
station.active(True)

# Continually try to connect to WiFi access point
while not station.isconnected():

    # Try to connect to WiFi access point
    print("Connecting...")
    station.connect(wifi_ssid, wifi_password)

    # Check to see if our REPL button is pressed over 10 seconds
    for i in range(100):
        if repl_button.value() == 0:
            print("Dropping to REPL")
            repl_led.value(1)
            sys.exit()
        utime.sleep_ms(100)

# Continually print out HTML from web page as long as we have a connection
while station.isconnected():

    # Display connection details
    print("Connected!")
    print("My IP Address:", station.ifconfig()[0])

    # Perform HTTP GET request on a non-SSL web
    response = urequests.get(url)

    # Display the contents of the page
    print(response.text)

    # Check to see if our REPL button is pressed over 10 seconds
    for i in range(100):
        if repl_button.value() == 0:
            print("Dropping to REPL")
            repl_led.value(1)
            sys.exit()
        utime.sleep_ms(100)

# If we lose connection, repeat this main.py and retry for a connection
print("Connection lost. Trying again.")
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# WLAN Connect

try:
  import usocket as socket
except:
  import socket

from time import sleep

from machine import Pin, I2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#import BME280

# ESP32 - Pin assignment
#i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)


ssid = 'R2-D2'
password = '2QK384JVPX'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


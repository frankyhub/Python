"""
Zeichnen mit gamegrid
Kaffemaschine
========= TigerJython =========="""

from gamegrid import *

def pressEvent(e):
    global state
    loc = toLocationInGrid(e.getX(), e.getY())
    if loc == Location(1, 2): # off
        state = State.OFF
        led.show(0)
        coffee.hide()
    elif loc == Location(2, 2): # on
        if state == State.OFF:
            state = State.STANDBY
            led.show(1)
    elif loc == Location(4, 2): # stop
        if state == State.WORKING:
            state = State.STANDBY
            coffee.hide()
    elif loc == Location(5, 2): # work
        if state == State.STANDBY:
            state = State.WORKING
            coffee.show()
    setTitle("State: " + str(state))
    refresh()
        
State = enum("OFF", "STANDBY", "WORKING")
state = State.OFF
makeGameGrid(7, 11, 50, None, "sprites/espresso.png", False, 
             mousePressed = pressEvent)
show()
setTitle("State: " + str(state))
led = Actor("sprites/lightout.gif", 2)
addActor(led, Location(3, 3))
coffee = Actor("sprites/coffee.png")
addActor(coffee, Location(3, 6))
coffee.hide()
refresh()


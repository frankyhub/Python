"""
Zeichnen mit Turtle

========= TigerJython =========="""
from gturtle import *

def onMouseHit(x, y):
    fill(x, y)      
        
makeTurtle(mouseHit = onMouseHit)
hideTurtle()
addStatusBar(30)
setStatusText("Click to fill a region!")
  
repeat 12:
    repeat 6:
        forward(80)
        right(60)
    left(30)      


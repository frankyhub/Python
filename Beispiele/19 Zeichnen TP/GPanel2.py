"""
Zeichnen mit gpanel

========= TigerJython =========="""
from gpanel import *
from random import randint, random

def randomColor():
   r = randint(0, 255)
   g = randint(0, 255)
   b = randint(0, 255)
   return makeColor(r, g, b)

makeGPanel()
bgColor(randomColor())

for i in range(20):
   setColor(randomColor())
   move(random(), random())
   a = random() / 2
   b = random() / 2
   fillEllipse(a, b)

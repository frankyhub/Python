"""
Zeichnen mit gpanel

========= TigerJython =========="""
import math
from gpanel import *
makeGPanel(-2, 2, -2, 2)

for i in range(628):
   t = i / 100
   x = math.cos(2 * t)
   y = math.sin(7 * t)
   move(x, y)
   circle(0.1) 
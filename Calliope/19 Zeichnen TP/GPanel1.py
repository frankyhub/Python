"""
Zeichnen mit gpanel

========= TigerJython =========="""
from gpanel import *

makeGPanel(0, 20, 0, 20)

for i in range(21):
    line(i, 0, 20, i)


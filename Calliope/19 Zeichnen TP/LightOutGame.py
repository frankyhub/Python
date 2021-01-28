"""
Zeichnen mit gamegrid
LightOut Game
========= TigerJython =========="""
from gamegrid import *
            
def pressCallback(e):
     loc = toLocationInGrid(e.getX(), e.getY())
     locs  = [0] * 5
     locs[0] = Location(loc.x, loc.y)
     locs[1] = Location(loc.x, loc.y - 1)
     locs[2] = Location(loc.x, loc.y + 1)
     locs[3] = Location(loc.x - 1, loc.y)
     locs[4] = Location(loc.x + 1, loc.y)
 
     for i in range(5):
         a = getOneActorAt(locs[i])
         if a != None:
              a.showNextSprite()
     refresh()
     return True    

makeGameGrid(5, 5, 50, Color.black, False, 
     mousePressed = pressCallback)
setTitle("LightsOut")
for i in range(5):
     for k in range(5):
          lamp = Actor("sprites/lightout.gif", 2)
          addActor(lamp, Location(i, k))
          lamp.show(1)     
show()


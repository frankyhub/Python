"""
Roboter Simulation

========= TigerJython =========="""
from simrobot import *

RobotContext.useBackground("sprites/border.gif")
RobotContext.setStartPosition(250, 490)
  
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ls = LightSensor(SensorPort.S3)
robot.addPart(ls)
ls.activate(True)
gear.forward()

while not robot.isEscapeHit():
   v = ls.getValue()
   if v < 500:
      gear.leftArc(0.2)
   else:
      gear.rightArc(0.2)
   Tools.delay(100)     
robot.exit()
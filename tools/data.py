from gpiozero import MCP3008
from gpiozero import DistanceSensor

#gpio23 -> echo 220,220分壓
#gpio24 -> trig

sensor = DistanceSensor(23, 24)
lightSensor = MCP3008(7)

def getDistance():#回傳距離
    return sensor.distance*100;

def getLightValue():#回傳光線    
    return lightSensor.value * 1000
from mobirob.robot import Robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep


r = Robot()
r.set_left(80)
r.set_right(-80)
sleep(1)
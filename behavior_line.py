from robot import Robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep


r = Robot()
r.left_motor.setSpeed(150)
r.right_motor.setSpeed(150)
r.left_motor.run(Raspi_MotorHAT.FORWARD)
r.right_motor.run(Raspi_MotorHAT.FORWARD)
sleep(1)
from time import sleep
from gpiozero import DistanceSensor


print("Prepare GPIO Pins")
sensor_l = DistanceSensor(echo=17, trigger=27, queue_len=2)
sensor_r = DistanceSensor(echo=5, trigger=6, queue_len=2)

while True:
    print(f"left: {sensor_l.distance * 100}, "
          f"Right: {sensor_r.distance * 100}")
    sleep(0.1)
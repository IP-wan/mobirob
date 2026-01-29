from Raspi_MotorHAT import Raspi_MotorHAT
from gpiozero import DistanceSensor
import atexit
import leds_led_shim


class Robot:

    def __init__(self, motorhat_addr=0x6f):
        # Setup the motorhat with the passed in address
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        # получение локальных переменных для каждого двигателя
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)
        # настройка датчиков расстояния
        self.left_distance_sensor = DistanceSensor(echo=17, trigger=27,
                                                   queue_len=2)
        self.right_distance_sensor = DistanceSensor(echo=5, trigger=6,
                                                    queue_len=2)
        self.leds = leds_led_shim.Leds()
        atexit.register(self.stop_all)

    def convert_speed(self, speed):
        # Выбор режима работы
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        # Определение частоты вращения
        output_speed = (abs(speed) * 255) // 100
        return mode, int(output_speed)

    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)

    def stop_all(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
        # Сбрасываем значения светодиодов
        self.leds.clear()
        self.leds.show()
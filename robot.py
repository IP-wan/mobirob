from Raspi_MotorHAT import Raspi_MotorHAT
import atexit


class Robot:
    def __init__(self, motorhat_addr=0x6f):
        # Настройка HAT-платы в соответствии с переданным адрессом
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        # получение локальных переменных для каждого двигателя
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)
        # убедимся, что после завершения кода двигатели останавливаются
        atexit.register(self.stop_motors)

    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
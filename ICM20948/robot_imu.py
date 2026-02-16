from icm20948 import ICM20948


class RobotImu:
    def __init__(self):
        self._imu = ICM20948()

    def read_temperature(self):
        return self._imu.read_temperature()

    
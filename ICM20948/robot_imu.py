from icm20948 import ICM20948
from vpython import vector


class RobotImu:
    def __init__(self):
        self._imu = ICM20948()

    def read_temperature(self):
        return self._imu.read_temperature()

    def read_gyroscope(self):
        _, _, _, x, y, z = self._imu.read_accelerometer_gyro_data()
        return vector(x, y, z)


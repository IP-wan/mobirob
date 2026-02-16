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

    def read_accelerometer(self):
        accel_x, accel_y, accel_z, _, _, _ = (
            self._imu.read_accelerometer_gyro_data())
        return vector(accel_x, accel_y, accel_z)

    def read_magnetometer(self):
        mag_x, mag_y, mag_z = self._imu.read_magnetometer_data()
        return vector(mag_x, -mag_y, -mag_z)
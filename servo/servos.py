from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM


class Servos:
    def __init__(self, addr=0x6f, deflect_90_in_ms=1):
        """addr: Адрес i2c микросхемы ШИМ.
        deflect_90_in_ms: устанавливаем значение, полученное при калибровке
        сервопривода.
        Это значение соответствует повороту на 90 градусов
        (длительность соответствующего импульса в миллисекундах)."""
        self._pwm = PWM(addr)
        # Устанавливаем временной базис
        pwm_frequency = 100
        self._pwm.setPWMFreq(pwm_frequency)
        # Устанавливаем длительность импульса для перехода в среднее положение
        # в миллисекундах.
        servo_mid_point_ms = 1.5
        # Частота равняется 1, разделенной на период, но, так как длина импульса
        # измеряется в миллисекундах, мы можем взять 1000.
        period_in_ms = 1000 / pwm_frequency
        # Микросхема отводит 4096 тактов на каждый период
        pulse_steps = 4096
        # Количество тактов на каждую миллисекунду.
        steps_per_ms = pulse_steps / period_in_ms
        # Такты на каждый градус.
        self.steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90
        # Импульс для перехода в среднее положение в тактах.
        self.servo_mid_point_steps = servo_mid_point_ms * steps_per_ms
        # Карта распределения каналов
        self.channels = [0, 1, 14, 15]

    def stop_all(self):
        # 0 означает отсутствие импульса, 4096 устанавливает бит, который
        # выключает выход (бит OFF).
        off_bit = 4096
        self._pwm.setPWM(self.channels[0], 0, off_bit)
        self._pwm.setPWM(self.channels[1], 0, off_bit)
        self._pwm.setPWM(self.channels[2], 0, off_bit)
        self._pwm.setPWM(self.channels[3], 0, off_bit)

    def _convert_degrees_to_steps(self, position):
        return int(self.servo_mid_point_steps + (position *
                                                 self.steps_per_degree))

    def set_servo_angle(self, channel, angle):
        """position: Положение от центра в градусах. От -90 до 90"""
        #Проверка
        if angle > 90 or angle < -90:
            raise ValueError("Угол за переделами допустимого диапазона")
        # Задаем положение
        off_step = self._convert_degrees_to_steps(angle)
        self._pwm.setPWM(self.channels[channel], 0, off_step)

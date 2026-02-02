from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM
import atexit


pwm = PWM(0x6f)
#Устанавливаем временной базис
pwm_frequency = 100
pwm.setPWMFreq(pwm_frequency)
# Устанавливаем длительность импульса для перехода в среднее положение
# в миллисекундах
servo_mid_point_ms = 1.5
# Вводим разницу длительности импульса для поворота на 90 градусов
# в миллисекундах
deflect_90_in_ms = 0.5
# Частота равняется 1, разделенной на период, но, так как длина импульса
# измеряется в миллисекундах, мы можем взять 1000
period_in_ms = 1000 / pwm_frequency
# Микросхема определяет 4096 тактов в каждом периоде
pulse_steps = 4096
# Количество тактов на каждую миллисекунду
steps_per_ms = pulse_steps / period_in_ms
# Такты на каждый градус
steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90
# Импульс для перехода в среднее положение в тактах
servo_mid_point_steps = servo_mid_point_ms * steps_per_ms

def convert_degrees_to_steps(position):
    return int(servo_mid_point_steps + (position * steps_per_degree))

atexit.register(pwm.setPWM, 0, 0, 4096)

while True:
    position = int(input("Type your position in degrees "
                         "(90 to -90, 0 is middle): "))
    end_step = convert_degrees_to_steps(position)
    pwm.setPWM(0, 0, end_step)
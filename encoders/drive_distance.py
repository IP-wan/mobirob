from robot import Robot, EncoderCounter
from pid_controller import PIController
import time
import logging


logger = logging.getLogger("drive_distance")

def drive_distance(bot, distance, speed=80):
    # Левый двигатель – главный, а правый - вторичный
    set_primary = bot.set_left
    primary_encoder = bot.left_encoder
    set_secondary = bot.set_right
    secondary_encoder = bot.right_encoder
    controller = PIController()
    # запускаем двигатели и цикл
    set_primary(speed)
    set_secondary(speed)

    while (primary_encoder.pulse_count < distance or
           secondary_encoder.pulse_count < distance):
        time.sleep(0.01)
        # Насколько мы отклонились?
        error = primary_encoder.pulse_count - secondary_encoder.pulse_count
        adjustment = controller.get_value(error)
        # Насколько быстро должны вращаться двигатели,
        # чтобы робот достиг нужной точки?
        set_primary(int(speed - adjustment))
        set_secondary(int(speed + adjustment))
        # Отладка
        logger.debug(f"Encoders: primary: {primary_encoder.pulse_count}, "
                     f"secondary: {secondary_encoder.pulse_count},"
                     f"e:{error} adjustment: {adjustment: .2f}")
        logger.info(f"Distances: primary: {primary_encoder.distance_in_mm()} "
                    f"mm, secondary: {secondary_encoder.distance_in_mm()} mm")


logging.basicConfig(level=logging.INFO)
bot = Robot()
distance_to_drive = 1000 # в мм – это метр
distance_in_ticks = EncoderCounter.mm_to_ticks(distance_to_drive)
drive_distance(bot, distance_in_ticks)
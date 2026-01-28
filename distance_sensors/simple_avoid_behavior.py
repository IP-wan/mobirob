from robot import Robot
from time import sleep


class ObstacleAvoidingBehavior:
    """Простой обход препятствий"""
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = 60

    def get_motor_speed(self, distance):
        """Этот метод вычисляет частоту вращения двигателя на основе
        данных о расстоянии, полученных от датчика"""
        if distance < 0.2:
            return -self.speed
        return self.speed

    def run(self):
        while True:
        # Получение показаний от датчика в метрах
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance
            print(f"Left: {left_distance:.2f}, Right: {right_distance:.2f}")
            left_speed = self.get_motor_speed(left_distance)
            self.robot.set_left(left_speed)
            right_speed = self.robot.right_distance_sensor.distance
            self.robot.set_right(right_speed)
            sleep(0.05)



bot = Robot()
behavior = ObstacleAvoidingBehavior(bot)
behavior.run()
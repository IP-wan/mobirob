from robot import Robot
from time import sleep
from led_rainbow import show_rainbow


bot = Robot()
while True:
    print("on")
    show_rainbow(bot.leds, range(bot.leds.count))
    bot.leds.show()
    sleep(0.5)
    print("of")
    bot.leds.clear()
    bot.leds.show()
    sleep(0.5)
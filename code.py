# Created by: Curtis Edwards
# Created on: Mar 2023
#
#  Uses a HC-SR04 Ultrasonic sensor to check the distance.

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP2)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

import RPi.GPIO as GPIO
from time import sleep


#PWM PIN
#ENA = 26
#ENB = 0

#GPIO PIN
motor1IN1 = 19
motor1IN2 = 13
motor2IN1 = 6
motor2IN2 = 5

def setPinConfig(INA):
    GPIO.setup(INA,GPIO.out)
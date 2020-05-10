import RPi.GPIO as GPIO
from time import sleep

#Motor LIST
MOTOR1 = 0
#MOTOR2 = 1
#MOTOR3 = 2
#MOTOR4 = 3

#Situation
Stop =0
Forward = 1
Backword = 2

#PWM PIN
#ENA = 26
#ENB = 0

#GPIO PIN
motor1IN1 = 19
motor1IN2 = 13
#motor2IN1 = 6
#motor2IN2 = 5

#PIN setting
HIGH = 1
LOW = 0



def setPinConfig(INA,INB):
    GPIO.setup(INA,GPIO.out)
    GPIO.setup(INB,GPIO.out)
    #control PWM 100Khz but L9910S not supported PWM
    #reuturn pwm
    
def setMotorControl(INA,INB,speed,situation):
    
    #pwm.ChangeDutyCycle(speed)
    
    #FORWARD
    if situation == Forward:
        GPIO.output(INA,HIGH)
        GPIO.output(INB,LOW)
    
    elif situation == Backword:
        GPIO.output(INA,LOW)
        GPIO.output(INB,HIGH)
    
    elif situation == Stop:
        GPIO.output(INA,LOW)
        GPIO.output(INB,LOW)
                
def setMotor(channel,speed,situation):
    if channel == MOTOR1:
        setMotorControl(motor1IN1,motor1IN2,speed,situation)
    #elif channel == MOTOR2:
    #    setMotorControl(motor2IN1,motor2IN2)
        
#Motor Control Main_method
GPIO.setmode(GPIO.BCM)
setPinConfig(motor1IN1,motor1IN2)


#Forward 80% Speed
setMotor(MOTOR1,80,Forward)
#delay
sleep(5)

#Forward 40% Speed
setMotor(MOTOR1,40,Backword)
#delay
sleep(5)

#STOP
setMotor(MOTOR1,80,Stop)

#END
GPIO.cleanup()
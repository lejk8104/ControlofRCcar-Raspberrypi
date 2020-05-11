import RPi.GPIO as GPIO
from time import sleep

#Motor LIST
MOTOR1 = 0
#MOTOR2 = 1


#status
Stop =0
Forward = 1
Backword = 2
Left = 3
Right = 4

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

#Movement Value
#Error = []

# Terminate Condition
Terminate = True
Keepgoing = False

line = 0
actural = 0


def isvaildPostion(line,actural):
    
    #Forward
    operation_list = []
    error = line - actural
    
    if line == actural:
        Movement = Forward
        Speed = 100
        
    #Right
    elif (error > 0 and error <= 15):
        Movement = Right
        Speed = 30
    elif (error >15  and error <= 30):
        Movement = Right
        Speed = 50
    
    elif (error >30):
        Movement = Right
        Speed = 70    
    #Left
    elif (error < 0 and error > -15):
        Movement = Left
        Speed = 30
    elif (error >15  and error <= 30):
          Movement = Left
          Speed = 50
    elif (error <-30):
          Movement = Left
          Speed = 70
    operation_list.append(Movement)
    operation_list.append(Speed)
    
    return operation_list

def setPinConfig(INA,INB):
    GPIO.setup(INA,GPIO.OUT)
    GPIO.setup(INB,GPIO.OUT)
    #control PWM 1000khz but L9910S not supported PWM
    #pwm = GPIO.PWM(EN, 1000)   #not define EN
    #pwm.start(0)
    
    #reuturn pwm
    
def setMotorControl(INA,INB,Speed,status):
    
    #pwm.ChangeDutyCycle(Speed)
    
    #Forward
    if status == Forward:
        GPIO.output(INA,HIGH)
        GPIO.output(INB,LOW)
    #Backword
    elif status == Backword:
        GPIO.output(INA,LOW)
        GPIO.output(INB,HIGH)
    #Stop
    elif status == Stop:
        GPIO.output(INA,LOW)
        GPIO.output(INB,LOW)
    
    # ISSUE Right and Left Mathod prameter is same for Forward
    #Right
    elif status == Right:
        GPIO.output(INA,HIGH)
        GPIO.output(INB,LOW)   
    #Left
    elif status == Left:
        GPIO.output(INA,HIGH)
        GPIO.output(INB,LOW)
               
def setMotor(channel,Speed,status):
    if channel == MOTOR1:
        setMotorControl(motor1IN1,motor1IN2,Speed,status)
    #else:
    #    setMotorControl(motor2IN1,motor2IN2)
        
#Motor Control Main_method
GPIO.setmode(GPIO.BCM)
setPinConfig(motor1IN1,motor1IN2)
#setPinConfig(motor2IN1,motor2IN2)


#END
while(True):
    Movement,Speed = isvaildPostion(line,actural)
    #Forward 100% Speed
    if (Movement == Forward):
        setMotor(MOTOR1,Speed,Movement)
        #setMotor(MOTOR2,Speed,Movement)
        #delay
        sleep(5)
    else:
        setMotor(MOTOR1,Speed,Movement)
        #setMotor(MOTOR2,Speed,Movement)
        #delay
        sleep(5)




    


#STOP
setMotor(MOTOR1,80,Stop)
#setMotor(MOTOR2,80,Stop)
sleep(5)
GPIO.cleanup()  
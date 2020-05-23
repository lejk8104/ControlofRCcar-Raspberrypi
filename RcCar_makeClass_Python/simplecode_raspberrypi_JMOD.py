import RPi.GPIO as GPIO
from time import sleep
import sys
import numpy as np

# =============================================================================
# using JMOD-Motor-Drive
#this version is able to control to two motor plz use it 
# =============================================================================

#define import package 
# if you import this codes, you can only be used in this range
#if __name__ == "__main__":

# define Motor LIST
MOTOR1 = 1      #Rear(Left) Wheel
MOTOR2 = 2      #Rear(Right) Wheel
#MOTOR3 = 3      #Front(Left) Wheel
#MOTOR4 = 4      #Front(Right) Wheel
    
#Situation
Stop =0
Forward = 1
Backword = 2
Left = 3
Right = 4
Break = 5

#PWM PIN
ENA = 26
ENB = 0

#GPIO PIN
motor1IN1 = 19
motor1IN2 = 13
motor2IN1 = 6
motor2IN2 = 5

#PIN setting
HIGH = 1
LOW = 0

#import other codes
# =============================================================================
# operation_array = np.empty((12,3), dtype =int)
# error = np.empty((6,1),dtype = int)
# =============================================================================

#test data
error = np.array([0,15,40,-15,-40,0])
operation_array = np.zeros((1,3), dtype =int)  #[Motor,Movement, DutyCycle]


def check_Array(operation_array,resultArray):
#     print("1",operation_array)
#     print("2",resultArray)
    if(operation_array[0][0] == 0):

        operation_array = operation_array+resultArray
#         print("init_array",operation_array)
    else:
        operation_array = np.concatenate((operation_array,resultArray),axis = 0)
#         print("Concatenate array",operation_array)
        
        #slicing only movement
        MovementArray = operation_array[0:,1:2]
#         print("Movement",MovementArray)
        length = MovementArray.shape[0] #shape vs len?
#         print("length",length)
        
        # define all motor is same dutycycle?
        mask = np.full((len(operation_array),1),MovementArray[0])
        
#         print("mask_setting",MovementArray[(mask== MovementArray)])
#        print(len(MovementArray[(mask== MovementArray)]))
        if length == len(MovementArray[(mask== MovementArray)]):
            dutycycle = RMSofDutyCycle(operation_array[0:,2:3])
            operation_array[0:2,length-1:length] = dutycycle
#     print("return",operation_array)
    return operation_array

#RMS is square of data's mean
def RMSofDutyCycle(Duty_array):
    return np.sqrt(np.mean(Duty_array**2))

# check the error and contrlling motor prameter
def isvaildPostion(error,operation_array):
    #Forward      
   if error == 0:
       print("forward setting")
       Movement = Forward
       DutyCycle1 = 100
       DutyCycle2 = 100
  #Right
   elif (error > 0 and error <= 15):
       print("Right setting")
       Movement = Right
       DutyCycle1 = 30
       DutyCycle2 = 0
   elif (error >15  and error <= 30):
       Movement = Right
       DutyCycle1 = 50
       DutyCycle2 = 0
   elif (error >30):
        Movement = Right
        DutyCycle1 = 70 
        DutyCycle2 = 0
    #Left
   elif (error < 0 and error > -15):
        Movement = Left
        DutyCycle1 = 0
        DutyCycle2 = 30
   elif (error >15  and error <= 30):
        Movement = Left
        DutyCycle1 = 0
        DutyCycle2 = 50
   elif (error <-30):
        Movement = Left
        DutyCycle1 = 0
        DutyCycle2 = 70
   resultArray = np.array([MOTOR1,Movement,DutyCycle1,MOTOR2,Movement,DutyCycle2]).reshape(2,3)
#    print(resultArray)
   operation_array = check_Array(operation_array,resultArray)
   
   # Remains the same size(operation_array()
   if operation_array.shape[0] > 6 :
       operation_array = np.delete(operation_array,[0,1], axis = 0)
   return operation_array 
      
def setPinConfig(ENable,INA,INB):
    GPIO.setup(ENable,GPIO.OUT)
    GPIO.setup(INA,GPIO.OUT)
    GPIO.setup(INB,GPIO.OUT)
        #control PWM 100Khz JMOD-motordriver is okay!
    currentPWM = 0
    pwm = GPIO.PWM(INB,100)
    pwm.start(currentPWM)
    return pwm

# maybe changed?
def movingRCcar(INA,INB): # this operation is same(Forward, Right, Left)
    GPIO.output(INA,HIGH)
    GPIO.output(INB,LOW)
    
def setMotorControl(INA,INB,last_pwm,DutyCycle,situation):
    PWM_Changeable = False
        # FORWARD
    if situation == Forward:
        print("situation is forward")
        movingRCcar(INA,INB)
        PWM_Changeable = True
        # BACKWORD
    elif situation == Backword:
        print("situation is Backword")
        GPIO.output(INA,LOW)
        GPIO.output(INB,HIGH)
        PWM_Changeable = True
        # STOP
    elif situation == Stop:
        GPIO.output(INA,LOW)
        GPIO.output(INB,LOW)
        PWM_Changeable = True
        # Right
    elif situation == Right:
#         print("situation is Right")
        movingRCcar(INA,INB)
        PWM_Changeable = True
        # Left
    elif situation == Left:
#         print("situation is Left")
        movingRCcar(INA,INB)
        PWM_Changeable = True
        """
        # Break
        elif situation == Break:
            print("situation is Break")
            GPIO.output(INA,HIGH)
            GPIO.output(INB,HIGH
            PWM_Changeable = True           
        """
        # setting Changed dutyCycle
    if PWM_Changeable == True:
        last_pwm.ChangeDutyCycle(DutyCycle)
        last_pwm = DutyCycle
        
def setMotor(channel,pwm,DutyCycle,situation):
    print("setMotor prameter",channel,pwm,DutyCycle,situation)
    if channel == MOTOR1:
        #print("motor1IN1",motor1IN1)
        #print("motor1IN2",motor1IN2)
        setMotorControl(motor1IN1,motor1IN2,pwm,DutyCycle,situation)
    else:
        setMotorControl(motor2IN1,motor2IN2,pwm,DutyCycle,situation)

#else:
        
# codes that is only use in the here
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pwm1 = setPinConfig(ENA, motor1IN1, motor1IN2)
pwm2 = setPinConfig(ENB, motor2IN1, motor2IN2)

#define endpoint of RcCar
terminatePoint= True

#Motor Control Main_method
while(terminatePoint):
    for error_i in error:
       operation_array = isvaildPostion(error_i,operation_array)
       # print(error_i)
       # print(operation_array)     
       #prameter setting
       length = len(operation_array)
       LeftMotor = operation_array[length-2:length-1,0:1][0][0]
       RightMotor = operation_array[length-1:length,0:1][0][0]
       DutyCycle1 = operation_array[length-2:length-1,1:2][0][0]
       DutyCycle2 = operation_array[length-1:length,1:2][0][0]
       Movement = operation_array[length-2:length-1,2:3][0][0]
       Movement = operation_array[length-1:length-0,2:3][0][0]
       print(LeftMotor)
       print(RightMotor)
       print(DutyCycle1)
       print(DutyCycle2)
       print(Movement)
       setMotor(LeftMotor,pwm1,DutyCycle1,Movement)
       setMotor(RightMotor,pwm2,DutyCycle2,Movement)
       sleep(2) 
       #STOP
       print("Stop init")
       setMotor(MOTOR1,pwm1,80,Stop)
       setMotor(MOTOR2,pwm2,80,Stop)
       sleep(2)    
    terminatePoint = False      
#END
GPIO.cleanup()
sys.exit()
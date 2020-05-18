import RPi.GPIO as GPIO
from time import sleep


if __name__ == "__main__":
    #Motor LIST
    MOTOR1 = 0
    MOTOR2 = 1
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
    motor1IN1 = 26
    motor1IN2 = 19
    motor2IN1 = 13
    motor2IN2 = 6
    
    #PIN setting
    HIGH = 1
    LOW = 0
    
    
    def setPinConfig(INA,INB):
        GPIO.setup(INA,GPIO.OUT)
        GPIO.setup(INB,GPIO.OUT)
        #control PWM 50Khz, and l9910s is using INB PWM pin 
        currentPWM = 0
        pwm = GPIO.PWM(INB,50)
        pwm.start(currentPWM)
        return pwm
        
    def setMotorControl(INA,INB,last_pwm,DutyCycle,situation):
        
        # FORWARD
        if situation == Forward:
            print("situation is forward")
            GPIO.output(INA,HIGH)
     
        # BACKWORD
        elif situation == Backword:
            print("situation is Backword")
            GPIO.output(INA,LOW)
    
        # STOP
        elif situation == Stop:
            GPIO.output(INA,LOW)
            GPIO.output(INB,LOW)
        
        # setting changed dutycycle    
        if last_pwm != DutyCycle:
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

else:
    #Motor Control Main_method
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pwm1 = setPinConfig(motor1IN1,motor1IN2)
    pwm2 = setPinConfig(motor2IN1,motor2IN2)
    #print("init pwm",pwm1)
    
    
    #Forward 80% Speed
    print("let's forward")
    setMotor(MOTOR1,pwm1,50,Forward)
    setMotor(MOTOR2,pwm2,50,Forward)
    print("forward after pwm",pwm1)
    #delay
    sleep(5)
    
    #Backword 40% Speed
    print("let's backword")
    
    setMotor(MOTOR1,pwm1,40,Backword)
    setMotor(MOTOR2,pwm2,40,Backword)
    #delay
    sleep(5)
    
    #STOP
    setMotor(MOTOR1,pwm1,80,Stop)
    setMotor(MOTOR2,pwm2,80,Stop)
    
    #END
    GPIO.cleanup()
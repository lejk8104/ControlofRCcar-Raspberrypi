import RPi.GPIO as GPIO
from time import sleep

if __name__ == "__main__":
    #Motor LIST
    MOTOR1 = 0
    MOTOR2 = 1
    
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
    motor1IN1 = 26       #DIR pin 
    motor1IN2 = 19       #PWM pin
    motor2IN1 = 13      #DIR pin      
    motor2IN2 = 6       ##PWM pin
    
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
            DutyCycle = 100
            
        #Right
        elif (error > 0 and error <= 15):
            Movement = Right
            DutyCycle = 30
        elif (error >15  and error <= 30):
            Movement = Right
            DutyCycle = 50
        
        elif (error >30):
            Movement = Right
            DutyCycle = 70    
        #Left
        elif (error < 0 and error > -15):
            Movement = Left
            DutyCycle = 30
        elif (error >15  and error <= 30):
              Movement = Left
              DutyCycle = 50
        elif (error <-30):
              Movement = Left
              DutyCycle = 70
        operation_list.append(Movement)
        operation_list.append(DutyCycle)
        
        return operation_list
    
    def setPinConfig(INA,INB):
        GPIO.setup(INA,GPIO.OUT)
        GPIO.setup(INB,GPIO.OUT)
        #control PWM 50Khz, and l9910s is using INB PWM pin 
        currentPWM = 0
        pwm = GPIO.PWM(INB,50)
        pwm.start(currentPWM)
        return pwm
    
    
    """
    def forward(INA,INB,CurrentPWM,lastPWM):
        
        GPIO.output(INA,HIGH)
        GPIO.output(INB,LOW) 
        if CurrentPWM != lastPWM:
            pwm.ChangeDutyCycle(CurrentPWM)
        print()
        """
        
        
    def setMotorControl(INA,INB,last_pwm,DutyCycle,situation):
        
        #Forward
        if situation == Forward:
            print("situation is forward")
            GPIO.output(INA,HIGH)
        #Backword
        elif situation == Backword:
            GPIO.output(INA,LOW)
            """
        #Stop
        elif situation == Stop:
            print("situation is Backword")
            GPIO.output(INA,LOW)
            """
        # ISSUE Right and Left Mathod prameter is same for Forward
        #Right
        elif situation == Right:
            print("situation is Right")
            GPIO.output(INA,HIGH)  
        #Left
        elif situation == Left:
            print("situation is left")
            GPIO.output(INA,HIGH)
    
           
        # setting changed dutycycle    
        if last_pwm != DutyCycle:
            last_pwm.ChangeDutyCycle(DutyCycle)        
            last_pwm = DutyCycle        
            
    def setMotor(channel,pwm,DutyCycle,situation):
        #print("setMotor prameter",channel,pwm,DutyCycle,situation)
        if channel == MOTOR1:
            setMotorControl(motor1IN1,motor1IN2,pwm,DutyCycle,situation)
        else:
            setMotorControl(motor2IN1,motor2IN2,pwm,DutyCycle,situation)
            
else:      
    #Motor Control Main_method
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print("GPIO init")
    pwm1 = setPinConfig(motor1IN1,motor1IN2)
    pwm2 = setPinConfig(motor2IN1,motor2IN2)
    #print("init pwm",pwm1)


    while(True):
        line = int(input("enter your line postion \n"))
        print("if your want to terminate this program, enter 7")
        actural = int(input("enter your line postion \n"))
        if actural == 7:
            break
        else:
            Movement,DutyCycle = isvaildPostion(line,actural)
            setMotor(MOTOR1,pwm1,DutyCycle,Movement)
            setMotor(MOTOR2,pwm2,DutyCycle,Movement)
            #Forward 100% DutyCycle
    
    #STOP
    setMotor(MOTOR1,80,Stop)
    #setMotor(MOTOR2,80,Stop)
    sleep(5)
    GPIO.cleanup()  
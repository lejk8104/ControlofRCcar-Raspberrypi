#include <wiringPi.h>
#include <softPwm.h>  /* include header file for software PWM */

//pwmPin
#define motor1_enable 5
#define motor2_enable 10

//motor1Pin
#define motor1_pin1 6
#define motor1_pin2 7

//motor2Pin
#define motor2_pin1 8
#define motor2_pin2 9


#define PWM 100

#define Value1 10
#define Value2 30
class RcCar
{
	

	void setup() {
		pinMode(motor1_pin1, OUTPUT);			//Connect Motor1pin1 to GPIO 5
		pinMode(motor1_pin2, OUTPUT);			//Connect Motor1pin2 to GPIO 6
		pinMode(motor1_enable, OUTPUT);			//Connect Motor1PWM to GPIO 7

		pinMode(motor2_pin1, OUTPUT);			//Connect Motor2pin1 to GPIO 8
		pinMode(motor2_pin2, OUTPUT);			//Connect Motor2pin2 to GPIO 9
		pinMode(motor2_enable, OUTPUT);			//Connect Motor1PWM to GPIO 10

		softPwmCreate(motor1_enable, 0, PWM);	//define PWM 0~100
		softPwmCreate(motor2_enable, 0, PWM);	//define PWM 0~100
	}

	void Forward(int Value1, int Value2) {

		softPwmWrite(motor1_enable, Value1);
		digitalWrite(motor1_pin1, LOW);		// Motor1 enable
		digitalWrite(motor1_pin2, HIGH);

		softPwmWrite(motor2_enable, Value2);
		digitalWrite(motor2_pin1, LOW);		// Motor1 enable
		digitalWrite(motor2_pin2, HIGH);
	}

	void Backward(int Value1, int Value2) {


		softPwmWrite(motor1_enable, Value1);
		digitalWrite(motor1_pin1, HIGH);		// Motor1 enable
		digitalWrite(motor1_pin2, LOW);

		softPwmWrite(motor2_enable, Value2);
		digitalWrite(motor2_pin1, HIGH);		// Motor1 enable
		digitalWrite(motor2_pin2, LOW);


	}
	void Left(int Value1, int Value2) {			//if angle A

		softPwmCreate(motor1_enable, 0, Value1);
		softPwmCreate(motor2_enable, 0, Value2);
	}
};


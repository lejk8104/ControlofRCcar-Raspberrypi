#include <wiringPi.h>
#include <softPwm.h>  /* include header file for software PWM */

//motor1Pin
#define motor1_pin1 6
#define motor1_pin2 7

//motor2Pin
#define motor2_pin1 24
#define motor2_pin2 23


int main() {

	//setup GPIO
	if (wiringPiSetupGpio() == -1) {		//pin_init not working
		return 1;
	}
	
	setup();
	forward();

	return 0;
}

void setup() {
	pinMode(motor1_pin1, OUTPUT);			//Connect Motor1pin1 to GPIO 5
	pinMode(motor1_pin2, OUTPUT);			//Connect Motor1pin2 to GPIO 6
	/*
	pinMode(motor1_enable, OUTPUT);			//Connect Motor1PWM to GPIO 7

	pinMode(motor2_pin1, OUTPUT);			//Connect Motor2pin1 to GPIO 8
	pinMode(motor2_pin2, OUTPUT);			//Connect Motor2pin2 to GPIO 9
	pinMode(motor2_enable, OUTPUT);			//Connect Motor1PWM to GPIO 10

	softPwmCreate(motor1_enable, 0, PWM);	//define PWM 0~100
	softPwmCreate(motor2_enable, 0, PWM);
	*/
}


void forward() {

	digitalWrite(motor1_pin1, LOW);
	digitalWrite(motor1_pin2, HIGH);

	/*
	softPwmWrite(motor1_enable, value1);

	softPwmWrite(motor2_enable, value2);
	digitalWrite(motor2_pin1, LOW);
	digitalWrite(motor2_pin2, HIGH);
	*/
}


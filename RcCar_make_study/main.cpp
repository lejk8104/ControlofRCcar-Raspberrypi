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

/*
#define motor3_enable 5
#define motor4_enable 10

//motor3Pin
#define motor1_pin1 6
#define motor1_pin2 7

//motor4Pin
#define motor2_pin1 8
#define motor2_pin2 9
*/

#define PWM 100


int pin [] = {0, motor1_pin1,motor1_pin2,motor2_pin1,motor2_pin2};
enum {Go, BACK, STOP, RIGHT, LEFT};
int value[] = { 0, 10, 20, 40, 80, 100 };
int error[] = { -2,-1,0,1,2 ,10};

int main(){

	//setup GPIO
	if (wiringPiSetupGpio() == -1) {		//pin_init not working
		return 1;
	}

	//setup pin
	setup();

	int i = 0;
	while (i<10) {

		switch (error[i]) {
			case '-2':
				right(value[1], value[5]);
				delay(1000);
				break;
			case '-1':
				right(value[2], value[4]);
				break;
			case '0':
				forward(value[5], value[5]);
				break;
			case '1':
				left(value[4], value[2]);
				break;
			case '2':
				left(value[5], value[1]);
				break;
			case '10':
				stop();
				break;
		}
	}
	return 0;
}
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


void forward(int value1, int value2) {
	softPwmWrite(motor1_enable, value1);
	digitalWrite(motor1_pin1, LOW);		
	digitalWrite(motor1_pin2, HIGH);

	softPwmWrite(motor2_enable, value2);
	digitalWrite(motor2_pin1, LOW);		
	digitalWrite(motor2_pin2, HIGH);
}

void backward(int value1, int value2) {
	softPwmWrite(motor1_enable, value1);
	digitalWrite(motor1_pin1, HIGH);		
	digitalWrite(motor1_pin2, LOW);

	softPwmWrite(motor2_enable, value2);
	digitalWrite(motor2_pin1, HIGH);		
	digitalWrite(motor2_pin2, LOW);
}
void stop()
{
	softPwmWrite(motor1_enable, 0);
	digitalWrite(motor1_pin1, LOW);		
	digitalWrite(motor1_pin2, HIGH);

	softPwmWrite(motor2_enable, 0);
	digitalWrite(motor2_pin1, LOW);		
	digitalWrite(motor2_pin2, HIGH);
}


void right(int value1, int value2) {
	if (value1 < value2) {
	}
	else {
		softPwmWrite(motor1_enable, value1);
		digitalWrite(motor1_pin1, LOW);		
		digitalWrite(motor1_pin2, HIGH);

		softPwmWrite(motor2_enable, value2);
		digitalWrite(motor2_pin1, LOW);		
		digitalWrite(motor2_pin2, HIGH);
	}
}

void left(int value1, int value2) {
	if (value2 < value1) {
	}
	softPwmWrite(motor1_enable, value1);
	digitalWrite(motor1_pin1, LOW);		
	digitalWrite(motor1_pin2, HIGH);

	softPwmWrite(motor2_enable, value2);
	digitalWrite(motor2_pin1, LOW);		
	digitalWrite(motor2_pin2, HIGH);
}


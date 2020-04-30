#include "RcCar.h"




int main(void)
{
	if (wiringPiSetupGpio() == -1)		//WringPI Setup____: init
	{
		return 1;
	}
	setup();
	while (true)
	{

	}


	return 0;

}

